# contains bunch of buggy examples
# taken from
# https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
import subprocess
import base64
import flask


# Input injection
def transcode_file(request, filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command)  # a bad idea! (? maybe fixed by @benko325)


# Assert statements
def asserts(request, user):
    assert user.is_admin, 'user does not have access'
    # secure code...


# Pickles
class RunBinSh(object):
    """Some pickles class"""
    def __reduce__(self):
        """Reduce those pickles"""
        return subprocess.Popen, (('/bin/sh',),)


def import_urlib_version(version):
    exec("import urllib%s as urllib" % version)


@app.route('/')
def index():
    module = flask.request.args.get("module")
    import_urlib_version(module)


pickle = RunBinSh()
print(base64.b64encode(pickle.dumps(RunBinSh())))
