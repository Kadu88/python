class GitRepository:

    def __init__(self, name, linguagem_repo, stars_qtd, url_repository, commits_total_repo, commits_url, developers, core_developers, idade_repo):
        self.name = name
        self.linguagem_repo = linguagem_repo
        self.stars_qtd = stars_qtd 
        self.url_repository = url_repository
        self.commits_total_repo = commits_total_repo
        self.commits_url = commits_url
        self.developers = developers
        self.core_developers = core_developers
        self.idade_repo = idade_repo

    def set_name(self, name):
        self.name = name

    def set_linguagem_repo(self, linguagem_repo):
        self.linguagem_repo = linguagem_repo

    def set_stars_qtd(self, stars_qtd):
        self.stars_qtd = stars_qtd

    def set_url_repository(self, url_repository):
            self.url_repository = url_repository

    def set_commits_total_repo(self, commits_total_repo):
        self.commits_total_repo = commits_total_repo

    def set_commits_url(self, commits_url):
        self.commits_total_repo = commits_url

    def set_developers(self, developers):
        self.developers = developers

    def set_core_developers(self, core_developers):
        self.core_developers = core_developers

    def set_idade_repo(self, idade_repo):
        self.idade_repo = idade_repo
