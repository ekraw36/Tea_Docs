import tea

data_path = "./co2.csv" 
tea.data(data_path, key='id')

variables = [
    {
        'name': 'Plant',
        'data type': 'nominal',
        'categories': ['Qn1', 'Qn2', 'Qn3', 'Qc1', 'Qc2', 'Qc3']
    },
    {
        'name': 'Type',
        'data type': 'nominal',
        'categories': ['Quebec', 'Mississippi']
    },
    {
        'name': 'Treatment',
        'data type': 'nominal',
        'categories': ['nonchilled', 'chilled']
    },
    {
        'name': 'conc',
        'data type': 'ratio'
    },
    {
        'name': 'uptake',
        'data type': 'ratio'
    }
]

tea.define_variables(variables)

study_design = {
    'study type': 'observational study',
    'contributor variables': 'Plant',
    'outcome variables': 'uptake'
}

tea.define_study_design(study_design)

tea.hypothesize(['Plant', 'uptake'], ['Plant: Qn1 < Qn2', 'Plant: Qc2 < Qc3'])

assumptions = {
    'Type I (False Positive) Error Rate': 0.05,
}

tea.assume(assumptions)