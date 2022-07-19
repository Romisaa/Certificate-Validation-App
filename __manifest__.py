{
    'name': "Validation Certificate App",
    'depends': ['base', 'crm'],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/sequence_data.xml",
        "views/certificate_view.xml",
        "views/certificate_type_view.xml",
        "views/traffic_department_view.xml",
        "views/customers.xml",
        "reports/report.xml",
        "reports/certificate_details.xml"

    ]
}
