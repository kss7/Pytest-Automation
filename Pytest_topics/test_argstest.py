
def test_argtest01(CmdOpt):
    #print ("Read config file: " + CmdOpt.readline())
    assert CmdOpt.readline().index('Lab')