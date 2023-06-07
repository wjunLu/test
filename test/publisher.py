import click
import docker
import wget

class publisher:
    repo = ""
    version = ""
    docker_file = ""
    download_url = ""
    
    def __init__(self, repo, version):
        self.repo = repo
        self.version = version

    def build(self):
        print("runing building task...")
        client = docker.from_env()
        client.images.build(path = '.', tag = 'my-latest-tag')
        print("Finished!\n")
    
    def download(self):
        self.download_url = "http://repo.openeuler.org/openEuler-" + self.version + \
            "/docker_img/aarch64/openEuler-docker.aarch64.tar.xz"
        print("Download docker image from %s" % self.download_url)
        wget.download(self.download_url)
        print("\nDownload successfully.\n")

    def push(self):
        print("runing publisher_push...")

    def check(self):
        print("runing publisher_check...")

        print("result: repo<%s>, version<%s>" % (self.repo, self.version))


@click.group()
@click.option("--repo", default = "openeuler/openeuler", help = "input repo")
@click.option("--version", default = "20.03-LTS", help = "input version")
@click.pass_context
def publisher_group(ctx, repo, version):
    ctx.obj = {'repo' : repo, 
               'version' : version}

@click.command()
@click.pass_context
def download(ctx):
    obj = publisher(ctx.obj['repo'], ctx.obj['version'])
    obj.download()

@click.command()
@click.pass_context
def build(ctx):
    obj = publisher(ctx.obj['repo'], ctx.obj['version'])
    obj.build()

@click.command()
@click.pass_context
def check(ctx):
    obj = publisher(ctx.obj['repo'], ctx.obj['version'])
    obj.check()

@click.command()
@click.pass_context
def push(ctx):
    obj = publisher(ctx.obj['repo'], ctx.obj['version'])
    obj.push()

publisher_group.add_command(download)
publisher_group.add_command(build)
publisher_group.add_command(push)
publisher_group.add_command(check)

if __name__ == '__main__':
    publisher_group()