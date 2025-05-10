import jpype
import jpype.imports
import os

from agentarium.jvm import start_jvm
start_jvm()

from agentarium import ModelSettings as JModelSettings

class ModelSettings:
    def __init__(self):
        self._settings = JModelSettings()

    @property
    def num_of_agents(self):
        return self._settings.getNumOfAgents()

    @num_of_agents.setter
    def num_of_agents(self, value):
        self._settings.setNumOfAgents(value)

    @property
    def num_of_cores(self):
        return self._settings.getNumOfCores()

    @num_of_cores.setter
    def num_of_cores(selfself, value):
        self._settings.setNumOfCores(value)

    @property
    def num_of_ticks_to_run(self):
        return self._settings.getNumOfTicksToRun()

    @num_of_ticks_to_run.setter
    def num_of_ticks_to_run(self, value):
        self._settings.setNumOfTicksToRun(value)

    @property
    def num_of_warm_up_ticks(self):
        return self._settings.getNumOfWarmUpTicks()

    @num_of_warm_up_ticks.setter
    def num_of_warm_up_ticks(self, value):
        self._settings.setNumOfWarmUpTicks(value)

    @property
    def total_num_of_ticks(self):
        return self._settings.getTotalNumOfTicks()

    def _get_java_obj(self):
        return self._settings