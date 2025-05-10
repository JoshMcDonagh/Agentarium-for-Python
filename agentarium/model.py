import jpype
import jpype.imports
from jpype.types import *

from agentarium.jvm import start_jvm
start_jvm()

from agentarium import Model as JModel

class Model:
    def __init__(self, settings):
        self._java_model = JModel(settings._get_java_obj())

    def run(self):
        return self._java_model.run()
    