# -*- coding: utf-8 -*-
from .QuModLibs.Client import *
from .QuModLibs.Modules.UI.EnhancedUI import QEScreenNode
@AllowCall
def PlayerDiedEvent():
    MY_UI.createUI()
    clientApi.HideHealthGui(True)

@QEScreenNode.autoRegister("ui0.main")
class MY_UI(QEScreenNode):
    def __init__(self, namespace, name, param):
        QEScreenNode.__init__(self, namespace, name, param)
        # PS：得益于内部缓存优化机制，注解只会被完整的扫描一次，后续直接匹配历史目标，因此热更新可能无法计入新的注解。（或者禁用缓存，但不推荐）
    @QEScreenNode.OnClick("/panel/button")
    def onClose(self):
        Call("PlayerWantsDie",playerId)
        MY_UI.removeClsUI()
        clientApi.HideHealthGui(False)


@AllowCall
def removeui():
    MY_UI.removeClsUI()
    clientApi.HideHealthGui(False)