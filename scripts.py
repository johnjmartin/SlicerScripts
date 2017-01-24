

# Creating and translating a node -- 2017-01-24

createModelsLogic = slicer.modules.createmodels.logic()
modelNode = createModelsLogic.CreateCoordinate(20,2)
modelNode.SetName('TestNode')

#creating transform node
modelToRas = slicer.vtkMRMLLinearTransformNode()
modelToRas.SetName('modelToRas')
slicer.mrmlScene.AddNode(modelToRas)

modelToRasTransform = vtk.vtkTransform()
modelToRasTransform.PreMultiply()
modelToRasTransform.Translate(0, 100, 0)
modelToRasTransform.Update()
modelToRas.SetAndObserveTransformToParent(modelToRasTransform)

modelNode.SetAndObserveTransformNodeID(modelToRas.GetID())
