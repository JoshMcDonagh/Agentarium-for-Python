import jpype
import os

JAR_NAME = "Agentarium-for-Java-1.0-SNAPSHOT.jar"

def start_jvm():
    if not jpype.isJVMStarted():
        jar_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib', JAR_NAME))
        jpype.startJVM(classpath=[jar_path])
