from autokeras.stub import *
from tests.common import get_add_skip_model, get_concat_skip_model


def test_to_stub_model():
    model = get_add_skip_model()
    stub_model = to_stub_model(model)
    assert len(stub_model.layers) == 23


def test_to_stub_model2():
    model = get_concat_skip_model()
    stub_model = to_stub_model(model)
    assert len(stub_model.layers) == 29
