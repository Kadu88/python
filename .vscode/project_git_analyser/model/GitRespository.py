class GitRepository:

    def __init__(self, linguagem_repo, url_repository, commits_total_repo, developers, core_developers, idade_repo):
        self.linguagem_repo = linguagem_repo
        self.url_repository = url_repository
        self.commits_total_repo = commits_total_repo
        self.developers = developers
        self.core_developers = core_developers
        self.idade_repo = idade_repo

    def set_linguagem_repo(self, linguagem_repo):
        self.linguagem_repo = linguagem_repo

    def set_url_repository(self, url_repository):
            self.url_repository = url_repository

    def set_commits_total_repo(self, commits_total_repo):
        self.commits_total_repo = commits_total_repo

    def set_developers(self, developers):
        self.developers = developers

    def set_core_developers(self, core_developers):
        self.core_developers = core_developers

    def set_idade_repo(self, idade_repo):
        self.idade_repo = idade_repo
