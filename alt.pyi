from typing import Any, List, Dict, overload
from typing_extensions import Protocol


class Vector3:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def toDict(self) -> Dict[int]: ...
    def toList(self) -> List[int]: ...
    def length(self) -> float: ...
    def distance(self) -> float: ...

    def toDegrees(self, vec: Vector3) -> Vector3: ...
    def toRadians(self, vec: Vector3) -> Vector3: ...
    def isInRange(self, vec: Vector3) -> bool: ...

    @overload
    def add(self, vec: Vector3) -> Vector3: ...
    @overload
    def add(self, num: int) -> Vector3: ...
    @overload
    def add(self, num1: int, num2: int, num3: int) -> Vector3: ...
    @overload
    def add(self, list: List[int]) -> Vector3: ...

    @overload
    def cross(self, vec: Vector3) -> Vector3: ...
    @overload
    def cross(self, num: int) -> Vector3: ...
    @overload
    def cross(self, num1: int, num2: int, num3: int) -> Vector3: ...
    @overload
    def cross(self, list: List[int]) -> Vector3: ...

    @overload
    def div(self, vec: Vector3) -> Vector3: ...
    @overload
    def div(self, num: int) -> Vector3: ...
    @overload
    def div(self, num1: int, num2: int, num3: int) -> Vector3: ...
    @overload
    def div(self, list: List[int]) -> Vector3: ...

    @overload
    def dot(self, vec: Vector3) -> Vector3: ...
    @overload
    def dot(self, num: int) -> Vector3: ...
    @overload
    def dot(self, num1: int, num2: int, num3: int) -> Vector3: ...
    @overload
    def dot(self, list: List[int]) -> Vector3: ...

    @overload
    def sub(self, vec: Vector3) -> Vector3: ...
    @overload
    def sub(self, num: int) -> Vector3: ...
    @overload
    def sub(self, num1: int, num2: int, num3: int) -> Vector3: ...
    @overload
    def sub(self, list: List[int]) -> Vector3: ...

    @overload
    def mul(self, vec: Vector3) -> Vector3: ...
    @overload
    def mul(self, num: int) -> Vector3: ...
    @overload
    def mul(self, num1: int, num2: int, num3: int) -> Vector3: ...
    @overload
    def mul(self, list: List[int]) -> Vector3: ...

    def negative(self) -> Vector3: ...
    def normalize(self) -> Vector3: ...
    def angleTo(self, vector: Vector3) -> float: ...
    def angleToDegrees(self, vector: Vector3) -> float: ...


class BaseObjectType:
    Player: Any
    Vehicle: Any
    VoiceChannel: Any
    
class WorldObject(BaseObjectType):
    def pos() -> Vector3: ...
    def dimension() -> int: ...

class Entity(WorldObject):
    def all() -> List[Entity]: ...
    def id() -> int: ...
    def getById(id: int) -> Entity | None: ...
    def model() -> int: ...
    def netOwner() -> Player | None: ...
    def setNetOwner(player: Player, disableMigration: bool=None) -> None: ...
    def resetNetOwner(disableMigration: bool=None) -> None: ...
    @overload
    def rot() -> Vector3: ...
    @overload
    def rot(rot: Vector3) -> None: ...
    @overload
    def visible() -> bool: ...
    @overload
    def visible(visible: bool) -> None: ...
    def deleteStreamSyncedMeta(key: str) -> None: ...
    def getStreamSyncedMeta(key: str) -> Any: ...
    def setStreamSyncedMeta(key: str, value: Any) -> None: ...
    def hasStreamSyncedMeta(key: str) -> bool: ...
    def deleteSyncedMeta(key: str) -> None: ...
    def getSyncedMeta(key: str) -> Any: ...
    def setSyncedMeta(key: str, value: Any) -> None: ...
    def hasSyncedMeta(key: str) -> bool: ...

class Player(Entity):
    def all() -> List[Player]: ...
    @overload
    def spawn(x: int, y: int, z: int, delay: int) -> None: ...
    @overload
    def spawn(position: Vector3, delay: int) -> None: ...
    @overload
    def health() -> int: ...
    @overload
    def health(value: int) -> None: ...
    def dead() -> bool: ...
    @overload
    def armour() -> int: ...       
    @overload
    def armour(value: int) -> None: ...
    @overload
    def maxArmour() -> int: ...       
    @overload
    def maxArmour(value: int) -> None: ...
    def speed() -> float: ...
    @overload
    def model() -> int: ...
    @overload
    def model(value: Any) -> None: ...
    def clearBloodDamage() -> None: ...
    def headRot() -> Vector3: ...
    def name() -> str: ...
    def authToken() -> str: ...
    def hwidHash() -> int: ...
    def hwidExHash() -> int: ...
    def ip() -> str: ...
    def socialId() -> int: ...
    def connected() -> bool: ...
    def ping() -> int: ...
    def kick(reason: str) -> None: ...
    @overload
    def currentWeapon() -> int: ...
    @overload
    def currentWeapon(hash: int) -> None: ...
    def currentWeaponComponents() -> List[int]: ...
    def currentWeaponTintIndex() -> int: ...
    @overload
    def giveWeapon(weaponHash: int, ammoCount: int, equipNow: bool) -> None: ...
    @overload
    def giveWeapon(weaponName: str, ammoCount: int, equipNow: bool) -> None: ...
    @overload
    def removeWeapon(weaponHash: int) -> None: ...
    @overload
    def removeWeapon(weaponName: str) -> None: ...
    @overload
    def getWeaponTintIndex(weaponHash: int) -> None: ...
    @overload
    def getWeaponTintIndex(weaponName: str) -> None: ...
    def removeAllWeapons() -> None: ...
    def flashlightActive() -> bool: ...
    @overload
    def hasWeaponComponent(weapon: int, component: int) -> bool: ...
    @overload
    def hasWeaponComponent(weapon: str, component: int) -> bool: ...
    @overload
    def hasWeaponComponent(weapon: int, component: str) -> bool: ...
    @overload
    def hasWeaponComponent(weapon: str, component: str) -> bool: ...
    @overload
    def addWeaponComponent(weapon: int, component: int) -> bool: ...
    @overload
    def addWeaponComponent(weapon: str, component: int) -> bool: ...
    @overload
    def addWeaponComponent(weapon: int, component: str) -> bool: ...
    @overload
    def addWeaponComponent(weapon: str, component: str) -> bool: ...
    @overload
    def setWeaponTintIndex(weapon: int, tintIndex: int) -> None: ...
    @overload
    def setWeaponTintIndex(weapon: str, tintIndex: int) -> None: ...
    def jumping() -> bool: ...
    def inRagdoll() -> bool: ...
    def aiming() -> bool: ...
    def shooting() -> bool: ...
    def reloading() -> bool: ...
    def entityAimingOffset() -> Vector3: ...
    def entityAimingAt() -> Entity | None: ...
    def aimPos() -> Vector3: ...
    def setDateTime(second: int, minute: int, hour: int, day: int, month: int, year: int) -> None: ...
    def setWeather(weather: int) -> None: ...
    def vehicle() -> Vehicle | None: ...
    def inVehicle() -> bool: ...
    def seat() -> int: ...

class Vehicle(Entity):
    def all() -> List[Vehicle]: ...

    activeRadioStation: int
    bodyAdditionalHealth: int
    bodyHealth: int
    # customPrimaryColor: RGBA
    # customSecondaryColor: RGBA
    isPrimaryColorCustom: bool
    isSecondaryColorCustom: bool
    customTires: bool
    darkness: int
    dashboardColor: int
    daylightOn: int
    destroyed: bool
    dirtLevel: int
    driver: Player | None
    engineHealth: int
    engineOn: bool
    flamethrowerActive: bool
    frontWheels: int
    handbrakeActive: bool
    hasArmoredWindows: bool
    headlightColor: int
    interiorColor: int
    lightsMultiplier: int
    livery: int
    lockState: int
    manualEngineControl: bool
    modKit: int
    modKitsCount: int
    model: str | int
    neon: int
    # neonColor: RGBA
    nightlightOn: bool
    numberPlateIndex: int
    numberPlateText: str
    pearlColor: int
    petrolTankHealth: int
    primaryColor: int
    rearWheels: int
    repairsCount: int
    roofLivery: int
    roofState: bool
    secondaryColor: int
    sirenActive: bool
    # tireSmokeColor: RGBA
    wheelColor: int
    wheelType: int
    wheelsCount: int
    windowTint: int

    def doesWheelHasTire(wheelId: int) -> bool: ...
    def getAppearanceDataBase64() -> str: ...
    def getArmoredWindowHealth(windowId: int) -> int: ...
    def getArmoredWindowShootCount(windowId: int) -> int: ...
    def getAttached() -> Vehicle: ...
    def getAttachedTo() -> Vehicle: ...
    def getBumperDamageLevel(bumperId: int) -> int: ...
    def getDamageStatusBase64() -> str: ...
    def getDoorState(doorId: int) -> int: ...
    def getDoorState(extraId: int) -> bool: ...
    def getGamestateDataBase64() -> str: ...
    def getHealthDataBase64() -> str: ...
    def getMod(modType: int) -> int: ...
    def getModsCount(modType: int) -> int: ...
    def getPartBulletHoles(partId: int) -> int: ...
    def getPartDamageLevel(partId: int) -> int: ...
    def getScriptDataBase64() -> str: ...
    def getWheelHealth(wheelId: int) -> int: ...
    def isLightDamaged(lightId: int) -> bool: ...
    def isSpecialLightDamaged(specialLightId: int) -> bool: ...
    def isWheelBurst(wheelId: int) -> bool: ...
    def isWheelDetached(wheelId: int) -> bool: ...
    def isWheelOnFire(wheelId: int) -> bool: ...
    def isWindowDamaged(windowId: int) -> bool: ...
    def isWindowOpened(windowId: int) -> bool: ...
    def repair() -> None: ...
    def setAppearanceDataBase64(data: str) -> None: ...
    def setArmoredWindowHealth(windowId: int, health: int) -> None: ...
    def setArmoredWindowShootCount(windowId: int, count: int) -> None: ...
    def setBumperDamageLevel(bumperId: int, level: int) -> None: ...
    def setDamageStatusBase64(data: str) -> None: ...
    def setDoorState(doorId: int, state: int) -> None: ...
    def setExtra(extraId: int, state: int) -> None: ...
    def setGamestateDataBase64(data: str) -> None: ...
    def setHealthDataBase64(data: str) -> None: ...
    def setLightDamaged(lightId: int, isDamaged: bool) -> None: ...
    def setMod(modType: int, modId: int) -> None: ...
    def setPartBulletHoles(partId: int, count: int) -> None: ...
    def setPartDamageLevel(partId: int, level: int) -> None: ...
    def setRearWheels(wheelId: int) -> None: ...
    def setScriptDataBase64(data: str) -> None: ...
    def setSpecialLightDamaged(specialLightId: int, isDamaged: bool) -> None: ...
    def setWheelBurst(wheelId: int, state: bool) -> None: ...
    def setWheelDetached(wheelId: int, state: bool) -> None: ...
    def setWheelFixed(wheelId: int) -> None: ...
    def setWheelHasTire(wheelId: int, state: bool) -> None: ...
    def setWheelHealth(wheelId: int, health: int) -> None: ...
    def setWheelOnFire(wheelId: int, state: int) -> None: ...
    def setWheels(wheelType: int, wheelId: int) -> None: ...
    def setWindowDamaged(windowId: int, isDamaged: bool) -> None: ...
    def setWindowOpened(windowId: int, state: bool) -> None: ...
    def getByID(number: int) -> Vehicle | None: ...

def log(value: str) -> None: ...
