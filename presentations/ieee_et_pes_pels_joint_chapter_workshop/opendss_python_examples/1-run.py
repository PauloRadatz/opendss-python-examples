import py_dss_interface
dss = py_dss_interface.DSS()

dss.text(fr"compile [C:\PauloRadatz\GitHub\opendss-python-examples\feeder_models\IEEETestCases\123Bus\IEEE123Master.dss]")
dss.text("new Energymeter.m element=line.l115 terminal=1")
dss.text("set mode=snapshot")
dss.text("solve")

dss.text("Show Voltage LN Nodes")
result = dss.text("export voltages")