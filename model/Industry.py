import enum


class EnergySecondaryIndustry(enum.Enum):
    EnergyEquipment = "能源装备"
    OilAndGas = "石油与天然气"
    Coal = "煤炭"


class RawMaterialsSecondaryIndustry(enum.Enum):
    ChemicalMaterials = "化学原料"
    Chemicals = "化学制品"
    BuildingMaterials = "建筑材料"
    ContainerAndPackaging = "容器与包装"
    NonFerrousMetals = "有色金属"
    Steel = "钢铁"
    NonMetallicMiningAndProducts = "非金属采矿及制品"
    PaperAndForestry = "纸类与林业产品"


class Industry(enum.Enum):
    Energy = "能源"
    RawMaterials = "原材料"
    Industry = "工业"
    OptionalConsumption = "可选消费"
    MainConsumption = "主要消费"
    Medicine = "医药卫生"
    Financial = "金融地产"
    InformationTechnology = "信息技术"
    Telecom = "电信业务"
    Public = "公用事业"
