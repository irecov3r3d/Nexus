from nexus_lm.storage.metadata import MetadataStore

def test_storage_initialization():
    store = MetadataStore(":memory:")
    assert store.get_latest_report() is None

def test_storage_persistence():
    store = MetadataStore(":memory:")
    store.save_report({"status": "Factually Sound", "score": 4})
    latest = store.get_latest_report()
    assert latest is not None
    assert latest["status"] == "Factually Sound"
    assert latest["score"] == 4

def test_storage_clear_all():
    store = MetadataStore(":memory:")
    store.save_report({"status": "Test Report", "score": 10})
    latest = store.get_latest_report()
    assert latest is not None

    store.clear_all()
    latest_after_clear = store.get_latest_report()
    assert latest_after_clear is None
