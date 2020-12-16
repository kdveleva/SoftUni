from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware: list = []
    _software: list = []

    @staticmethod
    def find_hardware_by_name(name: str):
        try:
            hardware = [x for x in System._hardware if x.name == name][0]
            return hardware
        except IndexError:
            return

    @staticmethod
    def find_software_by_name(name: str):
        try:
            software = [x for x in System._software if x.name == name][0]
            return software
        except IndexError:
            return

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.find_hardware_by_name(hardware_name)
        if not hardware:
            return "Hardware does not exist"
        es = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(es)
            System._software.append(es)
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.find_hardware_by_name(hardware_name)
        if not hardware:
            return "Hardware does not exist"
        ls = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(ls)
            System._software.append(ls)
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.find_hardware_by_name(hardware_name)
        software = System.find_software_by_name(software_name)
        if hardware and software:
            System._software.remove(software)
            return hardware.uninstall(software)
        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_memory = sum([x.memory for x in System._hardware])
        total_capacity = sum([x.capacity for x in System._hardware])
        total_used_memory = sum([x.memory_consumption for x in System._software])
        total_used_space = sum([x.capacity_consumption for x in System._software])
        return f"""System Analysis
Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)}
Total Operational Memory: {total_used_memory} / {total_memory}
Total Capacity Taken: {total_used_space} / {total_capacity}"""

    @staticmethod
    def system_split():
        s = ""
        for hardware in System._hardware:
            s += f'''Hardware Component - {hardware.name}
Express Software Components: {len([x for x in hardware.software_components if x.type == "Express"])}
Light Software Components: {len([x for x in hardware.software_components if x.type == "Light"])}
Memory Usage: {int(sum([x.memory_consumption for x in hardware.software_components]))} / {int(hardware.memory)}
Capacity Usage: {int(sum([x.capacity_consumption for x in hardware.software_components]))} / {int(hardware.capacity)}
Type: {hardware.type}'''
            if len(hardware.software_components):
                s += f'''Software Components: {', '.join([x.name for x in hardware.software_components])}'''
            else:
                s += f'''Software Components: None'''
        return s
