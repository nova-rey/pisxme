"""Executable truth-table checks for the storage selector contract."""

def selector_state(storage_sel):
    if storage_sel not in (0, 1):
        raise ValueError(storage_sel)
    return {
        "u12_usb_target": "TUSB9261" if storage_sel == 0 else "JMS583",
        "u13_storage_target": "TUSB9261_SATA" if storage_sel == 0 else "JMS583_PCIE",
        "shared_lane0_owner": "TUSB9261" if storage_sel == 0 else "JMS583",
        "hs_oe": 0,
    }

def main():
    sata = selector_state(0)
    nvme = selector_state(1)
    assert sata["u12_usb_target"] == "TUSB9261"
    assert sata["u13_storage_target"] == "TUSB9261_SATA"
    assert nvme["u12_usb_target"] == "JMS583"
    assert nvme["u13_storage_target"] == "JMS583_PCIE"
    assert sata["shared_lane0_owner"] != nvme["shared_lane0_owner"]
    assert sata["hs_oe"] == nvme["hs_oe"] == 0
    assert selector_state(0) != selector_state(1)
    print("PASS storage selector truth table: SATA=0, NVMe=1")

if __name__ == "__main__":
    main()
