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
│   └── rq1-artifacts-type-per-input.csv
│   └── rq1-artifacts-type-per-input-info.csv
│   └── rq1-artifacts-type-per-tdma.csv
│   └── rq1-artifacts-type-per-td-type.csv
│   └── rq1-output-fmts.csv
│   └── rq1-output-info.csv
│   └── rq2-td-types-per-tdma.csv
│   ├── selected-artifacts.csv
│   └── selected-studies.csv
│   └── studies-and-artifacts.json
├── scripts
│   ├── helpers.py 
|   └── merging-studies-and-artifacts-datasets.ipynb
|   └── rq0-demographic-information.ipynb
│   └── rq1-automation-artifacts.ipynb
|   └── rq2-tdm-activities-td-type.ipynb
|   └── rq3-automation-artifacts-usage.ipynb
├── figures
│   ├── dem-studies-per-author-type.pdf
│   └── dem-studies-per-venue.pdf
│   └── dem-studies-per-year.pdf
│   └── rq1-artifacts-type-per-tdma.pdf
│   └── rq1-artifacts-type-per-td-type.pdf
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

## Description of the variables in ``selected-artifacts.csv``

| variable name                         | description                                                                                                                              |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| id                                    | ID of the artifact                                                                                                                       |
| studies_citing_artifact               | ID of the studies that mention the artifact; this variable relates artifacts to studies                                                  |
| name                                  | The name of the automation artifact                                                                                                      |
| link                                  | The link to the automation artifact                                                                                                      |
| type                                  | The software type of each automation artifact                                                                                            |
| run_stand_alone                       | Whether it is possible to run the automation artifacts as standalone                                                                     |
| input_info                            | The information used by each automation artifact to automate the task (e.g., source code)                                                |
| input_fmt                             | The format of the information used by the automation artifact (e.g., XML)                                                                |
| output_info                           | The information provided by the automation artifact after the automation process                                                         |
| output_fmt                            | The format of the information provided by the automation artifact (e.g., XML)                                                            |
| evidence                              | The type of evidence we found in the literature (e.g., industrial studies)                                                               |
| td_type                               | The types of TD that are supported by the automation artifact                                                                            |
| tdma                                  | The TDM activities that are supported by the automation artifact                                                                         |
| trigger                               | The type of trigger that starts the execution of the automation artifacts (e.g., human trigger)                                          |
| trigger-description                   | The description of the triggers (e.g., new commit)                                                                                       |
| interface-type                        | The type of interface provided by the automation artifact                                                                                |
| interface-subtype                     | The subtype of interface provided by the automation artifact (e.g., api (plugin for github))                                             |
| is-integrated                         | Whether we found evidence of integration among the automation artifacts and other automation artifacts                                   |
| is-integrated-using-interface-subtype | Indicates which available interface is used for integrating the artifact                                                                 |
| is-integrated-with                    | Indicates with which type of software the artifact is integrated (e.g., development tool)                                                |
| is-integrated-description             | A description about the integration in which the artifact is involved                                                                    |
| is-integrted-outcome                  | A description of the rationale for the integration of the artifact                                                                       |
| can-integrated                        | Whether the automation artifact could be integrated with other automation artifacts, considering the input/output format and information |
| other_comments                        | Other annotations about the artifact                                                                                                     |

## Running the data analysis

1. Install Docker and docker-compose
2. Open a terminal (e.g., Windows Powershell) and navigate to the folder where replication package is saved
3. Run ``docker compose build``
4. After the environment is installed, run ``docker compose up``
5. Open a browser and access ``localhost:8888/lab``
6. Run the cells in the file ``merging-studies-and-artifacts-datasets.ipynb``, to generate the file ``studies-and-artifacts.json``.
7. After the exectution, it is possible to run the analysis contained in each of the scripts files, which are saved in the folder ``scripts``. Those scripts are organized by research question (e.g., ``rq2-tdm-activities-td-type.ipynb``). 


## Contact

- Please use the following email addresses if you have questions:
    - :email: <j.p.biazotto@rug.nl>
