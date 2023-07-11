from ..jobsearch.bb_gt_web_automation.DuckDuckGo import DuckDuckGo
import pytest

@pytest.fixture
def setup_teardown():
    # setup code
    print("setup")
    ddg = DuckDuckGo()
    
    yield
    
    
    # teardown code
    print("teardown")

def test_example(setup_teardown):
    # example test
    ddg = setup_teardown
    create_account_link = ddg.search(query="indeed create account")
    assert 1 == 1
