from flask_restx import fields


def pydantic_to_flask_model(schema_class, namespace):
    """
    Converte um Pydantic Schema para um modelo Flask-RESTx
    """
    try:
        # Primeiro, obter o dicionário completo do schema
        schema_dict = schema_class.schema(by_alias=True)

        # Identificar o nome da classe atual
        schema_name = schema_class.__name__

        # Acessar as propriedades dentro de `$defs` usando o nome da classe
        if '$defs' in schema_dict and schema_name in schema_dict['$defs']:
            properties = schema_dict['$defs'][schema_name].get('properties', {})
        else:
            # Caso não tenha `$defs`, tentar acessar diretamente `properties`
            properties = schema_dict.get('properties', {})

    except KeyError as e:
        raise ValueError(f"Erro ao extrair propriedades do schema: {e}. O schema retornado foi: {schema_dict}")  # noqa

    # Construir o modelo para Flask-RESTx com as propriedades obtidas
    model_dict = {}
    for key, value in properties.items():
        field_type = value.get('type', 'string').capitalize()  # Use string como default se o tipo não for encontrado
        model_dict[key] = getattr(fields, field_type)(
            description=value.get('description', ''),
            required=key in schema_dict.get('required', [])
        )

    return namespace.model(schema_class.__name__, model_dict)
