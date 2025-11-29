"""
Generated API endpoints for IUCN Red List API v4.
Auto-generated from OpenAPI specification.
"""

API_ENDPOINTS = {
    "get_assessment_assessment_id": {
        "method": "GET",
        "path": "/api/v4/assessment/{assessment_id}",
        "summary": """Retrieves an assessment""",
        "description": """Returns assessment data for a supplied <code>assessment_id</code>. This endpoint returns the same assessment data that you would see on an assessment page on the IUCN Red List website. Accepts both la...""",
        "tags": ['Assessment'],
        "path_params": ['assessment_id'],
        "query_params": [],
        "requires_auth": True
    },
    "get_biogeographical_realms": {
        "method": "GET",
        "path": "/api/v4/biogeographical_realms/",
        "summary": """Returns a list of biogeographic realm codes""",
        "description": """List available biogeographical realms (e.g. Neotropical or Palearctic)...""",
        "tags": ['Biogeographical Realms'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_biogeographical_realms_code": {
        "method": "GET",
        "path": "/api/v4/biogeographical_realms/{code}",
        "summary": """Returns a collection of assessments for a biogeographical realm code""",
        "description": """Returns a list of the latest assessments for a given biogeographical realm. Results are paginated (100 assessments per page)....""",
        "tags": ['Biogeographical Realms'],
        "path_params": ['code'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct_in_the_wild', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_comprehensive_groups": {
        "method": "GET",
        "path": "/api/v4/comprehensive_groups/",
        "summary": """Returns a list of comprehensive groups""",
        "description": """List the available comprehensive groups....""",
        "tags": ['Comprehensive Groups'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_comprehensive_groups_name": {
        "method": "GET",
        "path": "/api/v4/comprehensive_groups/{name}",
        "summary": """Returns a collection of assessments for a comprehensive group name""",
        "description": """Returns a list of the latest assessments for an comprehensive group name. Results are paginated (100 assessments per page)....""",
        "tags": ['Comprehensive Groups'],
        "path_params": ['name'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct_in_the_wild', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_conservation_actions": {
        "method": "GET",
        "path": "/api/v4/conservation_actions/",
        "summary": """returns a list of conservation actions""",
        "description": """...""",
        "tags": ['Conservation Actions'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_conservation_actions_code": {
        "method": "GET",
        "path": "/api/v4/conservation_actions/{code}",
        "summary": """returns a collection of assessments for a conservation action code""",
        "description": """...""",
        "tags": ['Conservation Actions'],
        "path_params": ['code'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct_in_the_wild', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_countries": {
        "method": "GET",
        "path": "/api/v4/countries/",
        "summary": """Returns a list of countries by ISO alpha-2 code""",
        "description": """Return a list of countries...""",
        "tags": ['Countries'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_countries_code": {
        "method": "GET",
        "path": "/api/v4/countries/{code}",
        "summary": """Returns a collection of assessments for a given country ISO alpha-2 code""",
        "description": """Return the latest assessments for a given country code. Results are paginated (100 assessments per page)...""",
        "tags": ['Countries'],
        "path_params": ['code'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct_in_the_wild', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_faos": {
        "method": "GET",
        "path": "/api/v4/faos/",
        "summary": """Returns a list of FAOs""",
        "description": """List the available FAOs....""",
        "tags": ['FAOs'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_faos_code": {
        "method": "GET",
        "path": "/api/v4/faos/{code}",
        "summary": """Returns a collection of assessments for an FAO code""",
        "description": """Returns a list of the latest assessments for an FAO code. Results are paginated (100 assessments per page)....""",
        "tags": ['FAOs'],
        "path_params": ['code'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct_in_the_wild', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_green_status_all": {
        "method": "GET",
        "path": "/api/v4/green_status/all",
        "summary": """Returns a list of all Green Status assessments""",
        "description": """List all Green Status assessments....""",
        "tags": ['Green Status'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_growth_forms": {
        "method": "GET",
        "path": "/api/v4/growth_forms/",
        "summary": """Returns a list of growth forms""",
        "description": """List the available growth forms....""",
        "tags": ['Growth Forms'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_growth_forms_code": {
        "method": "GET",
        "path": "/api/v4/growth_forms/{code}",
        "summary": """Returns a collection of assessments for a given growth form code""",
        "description": """Returns a list of the latest assessments for a given growth form code. Results are paginated (100 assessments per page)...""",
        "tags": ['Growth Forms'],
        "path_params": ['code'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct_in_the_wild', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_habitats": {
        "method": "GET",
        "path": "/api/v4/habitats/",
        "summary": """Returns a list of habitat codes.""",
        "description": """List the available habitat codes as per the Habitats Classification Scheme (v3.1)...""",
        "tags": ['Habitats'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_habitats_code": {
        "method": "GET",
        "path": "/api/v4/habitats/{code}",
        "summary": """Returns a collection of assessments for a given habitat code""",
        "description": """Return the latest assessments for a given habitat code (e.g. Forest - Temperate or Marine Intertidal). These habitat codes correspond to the IUCN Red List Habitats Classification Scheme (v3.1)...""",
        "tags": ['Habitats'],
        "path_params": ['code'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct_in_the_wild', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_information_api_version": {
        "method": "GET",
        "path": "/api/v4/information/api_version",
        "summary": """Returns the current version number of the IUCN Red List of Threatened Species API""",
        "description": """...""",
        "tags": ['Information'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_information_red_list_version": {
        "method": "GET",
        "path": "/api/v4/information/red_list_version",
        "summary": """Returns the current IUCN Red List of Threatened Species version""",
        "description": """...""",
        "tags": ['Information'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_population_trends": {
        "method": "GET",
        "path": "/api/v4/population_trends/",
        "summary": """Returns a list of population trends""",
        "description": """...""",
        "tags": ['Population Trends'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_population_trends_code": {
        "method": "GET",
        "path": "/api/v4/population_trends/{code}",
        "summary": """Returns a collection of assessments for a given population trend code""",
        "description": """Return a list of the latest assessments based on a population trend (i.e. increasing, decreasing, stable or unknown)...""",
        "tags": ['Population Trends'],
        "path_params": ['code'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct_in_the_wild', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_red_list_categories": {
        "method": "GET",
        "path": "/api/v4/red_list_categories/",
        "summary": """Returns a list of Red List categories""",
        "description": """Returns a list of Red List categories. This endpoint returns categories for the current IUCN Red List
      Categories and Criteria (v3.1) as well as older versions (i.e. v2.3)...""",
        "tags": ['Red List Categories'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_red_list_categories_code": {
        "method": "GET",
        "path": "/api/v4/red_list_categories/{code}",
        "summary": """Returns a collection of assessments for a given Red List category code""",
        "description": """Returns a list of the latest assessments for a given Red List category code. Note that a code may not be unique across Categories and Criteria versions. Therefore, codes like “EX” will return assessme...""",
        "tags": ['Red List Categories'],
        "path_params": ['code'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct_in_the_wild', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_research": {
        "method": "GET",
        "path": "/api/v4/research/",
        "summary": """Returns a list of habitat codes.""",
        "description": """List the available research codes as per the Research Needed Classification Scheme (v1.0)...""",
        "tags": ['Research'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_research_code": {
        "method": "GET",
        "path": "/api/v4/research/{code}",
        "summary": """Returns a collection of assessments for a given research code""",
        "description": """Return the latest assessments for a given research code. These research codes correspond to the IUCN Red List Research Needed Classification Scheme (v1.0)...""",
        "tags": ['Research'],
        "path_params": ['code'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct_in_the_wild', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_scopes": {
        "method": "GET",
        "path": "/api/v4/scopes/",
        "summary": """returns a list of scopes""",
        "description": """Returns a list of assessment scopes...""",
        "tags": ['Scopes'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_scopes_code": {
        "method": "GET",
        "path": "/api/v4/scopes/{code}",
        "summary": """Returns a collection of assessments for a given scope code""",
        "description": """Returns a list of the latest assessments for a given geographic scope. Results are paginated (100 assessments per page)...""",
        "tags": ['Scopes'],
        "path_params": ['code'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct_in_the_wild', 'required': False, 'type': 'boolean'}],
        "requires_auth": True
    },
    "get_statistics_count": {
        "method": "GET",
        "path": "/api/v4/statistics/count",
        "summary": """Return count of the number of species with assessments""",
        "description": """Returns a count of the number of species which have assessments....""",
        "tags": ['Statistics'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_stresses": {
        "method": "GET",
        "path": "/api/v4/stresses/",
        "summary": """Returns a list of stressors""",
        "description": """Returns a list of stressors...""",
        "tags": ['Stresses'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_stresses_code": {
        "method": "GET",
        "path": "/api/v4/stresses/{code}",
        "summary": """returns a collection of assessments for a given stress code""",
        "description": """Returns a list of the latest assessments for a given stressor. Results are paginated (100 assessments per page)...""",
        "tags": ['Stresses'],
        "path_params": ['code'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct_in_the_wild', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_systems": {
        "method": "GET",
        "path": "/api/v4/systems/",
        "summary": """Returns a list of systems""",
        "description": """Returns a list of systems...""",
        "tags": ['Systems'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_systems_code": {
        "method": "GET",
        "path": "/api/v4/systems/{code}",
        "summary": """Returns a collection of assessments for a given system code""",
        "description": """Returns a list of the latest assessments for a given system Results are paginated (100 assessments per page)...""",
        "tags": ['Systems'],
        "path_params": ['code'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct_in_the_wild', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_taxa_sis_sis_id": {
        "method": "GET",
        "path": "/api/v4/taxa/sis/{sis_id}",
        "summary": """Returns a collection of assessments for a given SIS id""",
        "description": """Returns summary latest and historic assessment data for a given <code>SIS id</code>. This endpoint does not provide all assessment data that can be found from querying <code>api/v4/assessments/{assess...""",
        "tags": ['Taxa'],
        "path_params": ['sis_id'],
        "query_params": [],
        "requires_auth": True
    },
    "get_taxa_scientific_name": {
        "method": "GET",
        "path": "/api/v4/taxa/scientific_name",
        "summary": """Returns a collection of assessments for a given genus_name and species_name (i.e. Latin binomial) and optional infra_name (i.e. Latin trinomial)""",
        "description": """Returns summary latest and historic assessment data for a given <code>genus_name</code> and <code>species_name</code> and optional <code>infra_name</code>. This endpoint does not provide all assessmen...""",
        "tags": ['Taxa'],
        "path_params": [],
        "query_params": [{'name': 'genus_name', 'required': True, 'type': 'string'}, {'name': 'species_name', 'required': True, 'type': 'string'}, {'name': 'infra_name', 'required': False, 'type': 'string'}, {'name': 'subpopulation_name', 'required': False, 'type': 'string'}],
        "requires_auth": True
    },
    "get_taxa_kingdom": {
        "method": "GET",
        "path": "/api/v4/taxa/kingdom/",
        "summary": """Returns a list of all kingdom names""",
        "description": """Returns a collection of all kingdom names...""",
        "tags": ['Taxa'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_taxa_kingdom_kingdom_name": {
        "method": "GET",
        "path": "/api/v4/taxa/kingdom/{kingdom_name}",
        "summary": """Returns a collection of the latests assessments for a given kingdom_name""",
        "description": """Returns the latest assessments for the supplied kingdom. Results are paginated (100 assessments per page) ...""",
        "tags": ['Taxa'],
        "path_params": ['kingdom_name'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_taxa_phylum": {
        "method": "GET",
        "path": "/api/v4/taxa/phylum/",
        "summary": """Returns a list of all phylum names""",
        "description": """Returns a collection of all phylum names...""",
        "tags": ['Taxa'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_taxa_phylum_phylum_name": {
        "method": "GET",
        "path": "/api/v4/taxa/phylum/{phylum_name}",
        "summary": """Returns a collection of the latests assessments for a given phylum_name""",
        "description": """Returns the latest assessments for the supplied phylum. Results are paginated (100 assessments per page) ...""",
        "tags": ['Taxa'],
        "path_params": ['phylum_name'],
        "query_params": [{'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_taxa_class": {
        "method": "GET",
        "path": "/api/v4/taxa/class/",
        "summary": """Returns a list of all class names""",
        "description": """Returns a collection of all class names...""",
        "tags": ['Taxa'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_taxa_class_class_name": {
        "method": "GET",
        "path": "/api/v4/taxa/class/{class_name}",
        "summary": """Returns a collection of the latests assessments for a given class_name""",
        "description": """Returns the latest assessments for the supplied class. Results are paginated (100 assessments per page) ...""",
        "tags": ['Taxa'],
        "path_params": ['class_name'],
        "query_params": [{'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_taxa_order": {
        "method": "GET",
        "path": "/api/v4/taxa/order/",
        "summary": """Returns a list of all order names""",
        "description": """Returns a collection of the all order names...""",
        "tags": ['Taxa'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_taxa_order_order_name": {
        "method": "GET",
        "path": "/api/v4/taxa/order/{order_name}",
        "summary": """Returns a collection of the latests assessments for a given order_name""",
        "description": """Returns the latest assessments for the supplied order. Results are paginated (100 assessments per page)...""",
        "tags": ['Taxa'],
        "path_params": ['order_name'],
        "query_params": [{'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_taxa_family": {
        "method": "GET",
        "path": "/api/v4/taxa/family/",
        "summary": """Returns a list of all family names""",
        "description": """Returns a collection of the all family names...""",
        "tags": ['Taxa'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_taxa_family_family_name": {
        "method": "GET",
        "path": "/api/v4/taxa/family/{family_name}",
        "summary": """Returns a collection of the latests assessments for a given family_name""",
        "description": """Returns the latest assessments for the supplied family. Results are paginated (100 assessments per page) ...""",
        "tags": ['Taxa'],
        "path_params": ['family_name'],
        "query_params": [{'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_taxa_possibly_extinct": {
        "method": "GET",
        "path": "/api/v4/taxa/possibly_extinct",
        "summary": """Returns a collection of the all latest global assessments for taxa that are possibly extinct""",
        "description": """Returns a collection of all latest global assessments for taxa that are possibly extinct...""",
        "tags": ['Taxa'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_taxa_possibly_extinct_in_the_wild": {
        "method": "GET",
        "path": "/api/v4/taxa/possibly_extinct_in_the_wild",
        "summary": """Returns a collection of the all latest global assessments for taxa that are possibly extinct in the wild""",
        "description": """Returns a collection of all latest global assessments for taxa that are possibly extinct in the wild...""",
        "tags": ['Taxa'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_threats": {
        "method": "GET",
        "path": "/api/v4/threats/",
        "summary": """Returns a list of threats""",
        "description": """Returns a list of threat codes....""",
        "tags": ['Threats'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_threats_code": {
        "method": "GET",
        "path": "/api/v4/threats/{code}",
        "summary": """Returns a collection of assessments for a given threat code""",
        "description": """Returns the latest assessments for a given threat code. This will only return assessments for the threat code specified.  You will need to do additional requests for sub-threats e.g. a request for thr...""",
        "tags": ['Threats'],
        "path_params": ['code'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct_in_the_wild', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
    "get_use_and_trade": {
        "method": "GET",
        "path": "/api/v4/use_and_trade/",
        "summary": """Returns a list of use and trades""",
        "description": """Returns a list of use and trade codes....""",
        "tags": ['Use and Trade'],
        "path_params": [],
        "query_params": [],
        "requires_auth": True
    },
    "get_use_and_trade_code": {
        "method": "GET",
        "path": "/api/v4/use_and_trade/{code}",
        "summary": """Returns a collection of assessments for a given use and trade code""",
        "description": """Returns the latest assessments for a given use and trade code....""",
        "tags": ['Use and Trade'],
        "path_params": ['code'],
        "query_params": [{'name': 'page', 'required': False, 'type': 'integer'}, {'name': 'year_published', 'required': False, 'type': 'integer'}, {'name': 'latest', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct', 'required': False, 'type': 'boolean'}, {'name': 'possibly_extinct_in_the_wild', 'required': False, 'type': 'boolean'}, {'name': 'scope_code', 'required': False, 'type': 'integer'}],
        "requires_auth": True
    },
}
