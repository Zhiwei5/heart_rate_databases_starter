def test_tachycardia():
    """
    To test the max_difference function in the list_module
    """
    try:
        import pytest
        from heart_database.heartrate_database import tachycardia
    except ImportError:
        print("The necessary module for this test failed to import")
        return

    test_data1 = (0.047, 190)
    test_data2 = (3, 160)
    test_data3 = (45, 100)
    test_data4 = ()

    output1 = tachycardia(test_data1)
    output2 = tachycardia(test_data2)
    output3 = tachycardia(test_data3)
    output4 = tachycardia(test_data4)

    assert output1 == 1
    assert output2 == 1
    assert output3 == 0
    assert output4 is None
