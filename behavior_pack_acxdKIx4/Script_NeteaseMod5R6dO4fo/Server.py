# -*- coding: utf-8 -*-
from .QuModLibs.Server import *

downed_player_ids = set()
donot_try = False
srcId_safe = None
first_budiaoluo = None  
lijichongsheng = None
diepos = None
dieweidu = None


@Listen(Events.ActuallyHurtServerEvent)
def ActuallyHurtServerEvent(args):
    
    global srcId_safe
    global donot_try
    entityId = args["entityId"]
    srcId = args["srcId"]
    damage = args["damage"]
    cause = args["cause"]
    print(cause)
    if cause == "magic":
        pass
    else:
        comp = serverApi.GetEngineCompFactory().CreateEngineType(entityId)
        entityType = comp.GetEngineType()
        EntityTypeEnum = serverApi.GetMinecraftEnum().EntityType
        if entityType & EntityTypeEnum.Player == EntityTypeEnum.Player:   
            if srcId == "-1":
                comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
                health1 = comp.GetAttrValue(serverApi.GetMinecraftEnum().AttrType.HEALTH)
                if damage >= health1:
                    res = is_player_downed(entityId)
                    if res == False:
                        comp = serverApi.GetEngineCompFactory().CreateHurt(entityId)
                        comp.ImmuneDamage(True)
                        comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
                        comp.SetCommand("/playanimation @s animation.player.sleeping defaut 1000000",entityId)
                        comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
                        comp.SetPlayerMovable(False)
                        comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
                        comp.SetPlayerJumpable(False)
                        Call(entityId,"PlayerDiedEvent")
                        donot_try = True
                        comp = serverApi.GetEngineCompFactory().CreateName(entityId)
                        name = comp.GetName()
                        comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
                        comp.SetNotifyMsg("[系统]"+name+"已倒下，快去拿急救包救援！", serverApi.GenerateColor('BLUE'))
                        downed_player_ids.add(entityId)
            else:
                comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
                hurt = comp.GetEntityDamage(srcId,entityId)
                comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
                health = comp.GetAttrValue(serverApi.GetMinecraftEnum().AttrType.HEALTH)
        
                if hurt >= health:
                    res = is_player_downed(entityId)
                    print(res)
                    if res == False:
                        comp = serverApi.GetEngineCompFactory().CreateHurt(entityId)
                        comp.ImmuneDamage(True)
                        comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
                        comp.SetCommand("/playanimation @s animation.player.sleeping defaut 1000000",entityId)
                        comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
                        comp.SetPlayerMovable(False)
                        comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
                        comp.SetPlayerJumpable(False)
                        Call(entityId,"PlayerDiedEvent")
                        srcId_safe = srcId
                        donot_try = True
                        comp = serverApi.GetEngineCompFactory().CreateName(entityId)
                        name1 = comp.GetName()
                        comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
                        comp.SetNotifyMsg("[系统]"+name1+"已倒下，快去拿急救包救援！", serverApi.GenerateColor('BLUE'))
                        downed_player_ids.add(entityId)

@Listen(Events.ActorHurtServerEvent)
def ActorHurtServerEvent(args):
    global diepos
    global dieweidu
    global donot_try
    entityId = args["entityId"]
    cause = args["cause"]
    damage = args["damage"]
    print(cause)
    if cause == "magic":
        comp = serverApi.GetEngineCompFactory().CreateEngineType(entityId)
        entityType = comp.GetEngineType()
        EntityTypeEnum = serverApi.GetMinecraftEnum().EntityType
        if entityType & EntityTypeEnum.Player == EntityTypeEnum.Player:
            comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
            health1 = comp.GetAttrValue(serverApi.GetMinecraftEnum().AttrType.HEALTH)
            if damage >= health1:
                res = is_player_downed(entityId)
                if res == False:
                    comp = serverApi.GetEngineCompFactory().CreateHurt(entityId)
                    comp.ImmuneDamage(True)
                    comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
                    comp.SetCommand("/playanimation @s animation.player.sleeping defaut 1000000",entityId)
                    comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
                    comp.SetPlayerMovable(False)
                    comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
                    comp.SetPlayerJumpable(False)
                    Call(entityId,"PlayerDiedEvent")
                    donot_try = True
                    comp = serverApi.GetEngineCompFactory().CreateName(entityId)
                    name = comp.GetName()
                    comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
                    comp.SetNotifyMsg("[系统]"+name+"已倒下，快去拿急救包救援！", serverApi.GenerateColor('BLUE'))
                    downed_player_ids.add(entityId)
                    comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
                    diepos = comp.GetPos()
                    comp = serverApi.GetEngineCompFactory().CreateDimension(entityId)
                    dieweidu = comp.GetEntityDimensionId()
    if cause == "entity_explosion":
        comp = serverApi.GetEngineCompFactory().CreateEngineType(entityId)
        entityType = comp.GetEngineType()
        EntityTypeEnum = serverApi.GetMinecraftEnum().EntityType
        if entityType & EntityTypeEnum.Player == EntityTypeEnum.Player:
            comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
            health1 = comp.GetAttrValue(serverApi.GetMinecraftEnum().AttrType.HEALTH)
            if damage >= health1:
                res = is_player_downed(entityId)
                if res == False:
                    comp = serverApi.GetEngineCompFactory().CreateHurt(entityId)
                    comp.ImmuneDamage(True)
                    comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
                    comp.SetGameRulesInfoServer(ruleDict)
                    comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
                    comp.SetPlayerMovable(False)
                    comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
                    comp.SetPlayerJumpable(False)
                    Call(entityId,"PlayerDiedEvent")
                    donot_try = True
                    comp = serverApi.GetEngineCompFactory().CreateName(entityId)
                    name = comp.GetName()
                    comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
                    comp.SetNotifyMsg("[系统]"+name+"已倒下，快去拿急救包救援！", serverApi.GenerateColor('BLUE'))
                    downed_player_ids.add(entityId)
                    comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
                    comp.SetGameRulesInfoServer(ruleDict)
                    comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
                    succ = comp.EnableKeepInventory(True)

                    comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
                    diepos = comp.GetPos()
                    comp = serverApi.GetEngineCompFactory().CreateDimension(entityId)
                    dieweidu = comp.GetEntityDimensionId()
    if cause == "wither":
        comp = serverApi.GetEngineCompFactory().CreateEngineType(entityId)
        entityType = comp.GetEngineType()
        EntityTypeEnum = serverApi.GetMinecraftEnum().EntityType
        if entityType & EntityTypeEnum.Player == EntityTypeEnum.Player:
            comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
            health1 = comp.GetAttrValue(serverApi.GetMinecraftEnum().AttrType.HEALTH)
            if damage >= health1:
                res = is_player_downed(entityId)
                if res == False:
                    comp = serverApi.GetEngineCompFactory().CreateHurt(entityId)
                    comp.ImmuneDamage(True)
                    comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
                    comp.SetCommand("/playanimation @s animation.player.sleeping defaut 1000000",entityId)
                    comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
                    comp.SetPlayerMovable(False)
                    comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
                    comp.SetPlayerJumpable(False)
                    Call(entityId,"PlayerDiedEvent")
                    donot_try = True
                    comp = serverApi.GetEngineCompFactory().CreateName(entityId)
                    name = comp.GetName()
                    comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
                    comp.SetNotifyMsg("[系统]"+name+"已倒下，快去拿急救包救援！", serverApi.GenerateColor('BLUE'))
                    downed_player_ids.add(entityId)
                    comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
                    diepos = comp.GetPos()
                    comp = serverApi.GetEngineCompFactory().CreateDimension(entityId)
                    dieweidu = comp.GetEntityDimensionId()





@AllowCall
def PlayerWantsDie(playerId):
    comp = serverApi.GetEngineCompFactory().CreateName(playerId)
    name = comp.GetName()
    comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
    comp.SetNotifyMsg("[系统]"+name+"已放弃被救援", serverApi.GenerateColor('BLUE'))
    global donot_try
    global srcId_safe
    global diepos
    global dieweidu
    diepos = None
    dieweidu = None
    donot_try = False
    comp = serverApi.GetEngineCompFactory().CreateHurt(playerId)
    comp.ImmuneDamage(False)
    comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
    succ = comp.EnableKeepInventory(False)
    comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
    comp.SetCommand("/playanimation @s animation.player.sleeping defaut 1",playerId)
    
    print(srcId_safe)
    print("srcId_safe")
    if srcId_safe == None:
        comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
        comp.SetCommand("/kill @s",playerId)
        print("DIE!")
        comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
        comp.SetPlayerMovable(True)
        comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
        comp.SetPlayerJumpable(True)
        remove_downed_player(playerId)
        
        
    else:
        comp = serverApi.GetEngineCompFactory().CreateHurt(playerId)
        comp.Hurt(20, serverApi.GetMinecraftEnum().ActorDamageCause.EntityAttack, srcId_safe, None, False)
        comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
        comp.SetPlayerMovable(True)
        comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
        comp.SetPlayerJumpable(True)
        remove_downed_player(playerId)
        

@Listen(Events.PlayerDieEvent)
def PlayerDieEvent(args):
    global donot_try
    global srcId_safe
    srcId_safe = None
    donot_try = False

    
@Listen(Events.PlayerAttackEntityEvent)
def PlayerAttackEntityEvent(args):
    global srcId_safe
    global donot_try
    global diepos
    global dieweidu
    victimId = args["victimId"]
    playerId = args["playerId"]
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    dict = comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, 0)
    if dict and dict["newItemName"] == "xiaoshuihuixing:item_5":
        comp = serverApi.GetEngineCompFactory().CreateEngineType(victimId)
        entityType = comp.GetEngineType()
        EntityTypeEnum = serverApi.GetMinecraftEnum().EntityType
        if entityType & EntityTypeEnum.Player == EntityTypeEnum.Player:
            res = is_player_downed(victimId)
            print(res)
            if res == True:
                args["cancel"] = True
                comp = serverApi.GetEngineCompFactory().CreatePlayer(victimId)
                comp.SetPlayerMovable(True)
                comp = serverApi.GetEngineCompFactory().CreatePlayer(victimId)
                comp.SetPlayerJumpable(True)
                comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
                comp.SetCommand("/playanimation @s animation.player.sleeping defaut 1",victimId)
                comp = serverApi.GetEngineCompFactory().CreateName(victimId)
                victimIdName = comp.GetName()
                comp = serverApi.GetEngineCompFactory().CreateName(playerId)
                playerIdName = comp.GetName()
                comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
                comp.SetNotifyMsg("[系统]"+victimIdName+"已被"+playerIdName+"救起！", serverApi.GenerateColor('BLUE'))
                srcId_safe = None
                Call(victimId,"removeui")
                donot_try = False
                diepos = None
                dieweidu = None
                comp = serverApi.GetEngineCompFactory().CreatePlayer(victimId)
                succ = comp.EnableKeepInventory(False)
                comp = serverApi.GetEngineCompFactory().CreateHurt(victimId)
                comp.ImmuneDamage(False)
                remove_downed_player(victimId)

def remove_downed_player(entityId):
    if entityId in downed_player_ids:
        downed_player_ids.remove(entityId)
        return True
    return False        
    

def is_player_downed(entityId):
    return entityId in downed_player_ids  # 如果使用set


ruleDict ={
    'option_info': {
        'immediate_respawn': True,


    }
}

ruleDict1 ={
    'option_info': {
        'immediate_nrespaw': False,


    }
}


@Listen(Events.LoadServerAddonScriptsAfter)
def LoadServerAddonScriptsAfter(args):
    comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
    comp.AddRepeatedTimer(500,timergetrules)
    

@Listen(Events.PlayerRespawnFinishServerEvent)
def PlayerRespawnFinishServerEvent(args):
    global diepos
    global dieweidu
    global lijichongsheng
    global donot_try
    playerId = args["playerId"]
    res = is_player_downed(playerId)
    if res == True:
        comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
        comp.SetGameRulesInfoServer(ruleDict1)
        comp = serverApi.GetEngineCompFactory().CreateDimension(playerId)
        comp.ChangePlayerDimension(dieweidu, diepos)
        Call(playerId,"PlayerDiedEvent")
        comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
        comp.SetCommand("/playanimation @s animation.player.sleeping defaut 1000000",playerId)
        donot_try = False
        comp = serverApi.GetEngineCompFactory().CreateHurt(playerId)
        comp.ImmuneDamage(False)
        

def timergetrules():
    global lijichongsheng
    global donot_try
    if donot_try == False:
        comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
        type = comp.GetGameRulesInfoServer()
        immediate_respawn = type['option_info']['immediate_respawn']
        if immediate_respawn == True:
            lijichongsheng = True
        if immediate_respawn == False:
            lijichongsheng = False 



