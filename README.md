# Replication Package for Technical Debt Management Automation: State of the Art and Future Perspectives

##### Authors: Joao Paulo Biazotto, Daniel Feitosa, Elisa Yumi Nakagawa, and Paris Avgeriou

## Description of this study:

__Context__: Technical Debt (TD) refers to non-optimal decisions made in software projects
that may lead to short-term benefits, but potentially harm the system’s maintenance
and evolution in the long-term. Technical debt management (TDM) refers to a set of
activities that are performed to handle TD, e.g., identification, documentation, and
repayment of TD. These activities typically entail tasks such as code and architectural
analysis, which can be time-consuming if done manually. To address this, substantial
research work has focused on automating TDM tasks, such as automatic identification
of code smells and automatic refactoring of source code.

__Problem and Motivation__: There is a lack of studies that summarize current
approaches in TDM automation. This can hinder practitioners in selecting and using
optimal automation strategies in order to efficiently manage TD. It can also prevent
researchers from understanding the research landscape and addressing the research
problems that matter the most.

__Objective__: The main objective of this study is to provide an overview of the state of the
art in TDM automation, analyzing the available tools, their use, and the challenges in
automating TDM.

__Methods__: We conducted a systematic mapping study (SMS), following the guidelines
proposed by Kitchenham et al [1]. From an initial set of 1 086 primary studies, 178 were
selected to answer three research questions covering different facets of TDM
automation.

__Results__: We found 121 automation artifacts that can be used to automate TDM
activities. The artifacts were classified in 4 different types (i.e., tools, plugins, scripts,
and bots); the inputs/outputs and interfaces were also collected and reported. Finally, a
conceptual model is proposed that synthesizes the results and allows to discuss the
current state of TDM automation and related challenges.

__Conclusion__: The research community has investigated to a large extent how to
perform various TDM activities automatically, considering the number of studies and
automation artifacts we identified. Nonetheless, more research is needed towards fully
automated TDM, specially concerning the integration of the automation artifacts and
their use in software development

## Structure of the replication package:

The replication package includes the datasets (for selected studies and automation artifacts), the scripts for data analysis, and all the figures used in the manuscript.

```
├── data
│   ├── selected_artifacts.csv
│   └── studies_dataset.csv
│   └── rq1-output-fmts.csv
│   └── rq1-output-info.csv
│   └── Step1_artifacts.json
├── scripts
│   ├── rq1-automation-artifacts.jpynb
│   └── rq2-tdm-activities-td-type.jpynb
|   └── rq3-automation-artifacts-usage.jpynb
|   └── Step1-ConvertingCSVToJson.jpynb
├── figures
│   ├── dem-studies-per-author-type.pdf
│   └── dem-studies-per-venue.pdf
│   └── dem-studies-per-year.pdf
│   └── rq1-inuput-fmt.pdf
│   └── rq1-inuput-info.pdf
│   └── rq2-td-types.pdf
│   └── rq2-tdma.pdf
│   └── rq2-upset-td-types.pdf
│   └── rq2-upset-tdma.pdf
│   └── rq3-upset-existing-integration.pdf
│   └── rq3-upset-interfaces.pdf
│   └── rq3-upset-possible-integration.pdf
├── LICENSE.txt
├── README.md
├── docker-compose.yaml
├── Dockerfile
└── env.yaml

```

## Running data analysis

1. Install Docker and docker-compose
2. Open a terminal (e.g., Windows Powershell) and navigate to the folder where replication package is saved
3. Run ``docker compose build``
4. After the environment is installed, run ``docker compose up``
5. Open a browser and access ``localhost:8888/lab``
6. Run the cells in the file ``Step1-ConvertionCSVToJson.ipynb``
7. After the exectution, it is possible to run the analysis contained in each of the scripts in the folder ``scripts``


## Contact

- Please use the following email addresses if you have questions:
    - :email: <j.p.biazotto@rug.nl>
