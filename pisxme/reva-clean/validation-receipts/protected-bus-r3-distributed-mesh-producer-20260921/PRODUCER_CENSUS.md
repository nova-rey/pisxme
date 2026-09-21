# R3 distributed mesh census

{
  "status": "PRODUCER_CANDIDATE_REQUIRES_NATIVE_VALIDATION",
  "base_ref": "c574c287",
  "authority": "PISXME-P24-PROTECTED-BUS-MPA-EFFECTIVE-NETWORK-20260921-R1",
  "candidate_board": "pisxme/reva-clean/PHASE24_R3_DISTRIBUTED_MESH_CANDIDATE.kicad_pcb",
  "anchors_mm": {
    "J1": [
      150,
      90,
      0
    ],
    "J5": [
      12,
      25,
      0
    ],
    "J6": [
      12,
      50,
      0
    ],
    "J9": [
      12,
      75,
      0
    ]
  },
  "fuse_positions_mm": {
    "F1": [
      36,
      15,
      0
    ],
    "F2": [
      64,
      15,
      0
    ],
    "F3": [
      92,
      15,
      0
    ],
    "F4": [
      36,
      40,
      0
    ],
    "F5": [
      64,
      40,
      0
    ],
    "F6": [
      92,
      40,
      0
    ],
    "F7": [
      36,
      65,
      0
    ],
    "F8": [
      64,
      65,
      0
    ],
    "F9": [
      92,
      65,
      0
    ]
  },
  "holder_envelope_mm": 24.25,
  "bank_pitch_mm": 25.0,
  "interbank_gap_mm": 0.75,
  "positive_layers": [
    "F.Cu",
    "B.Cu",
    "In2.Cu"
  ],
  "return_layers": [
    "In1.Cu",
    "In4.Cu"
  ],
  "positive_transition_columns": [
    104,
    106.5,
    109,
    111.5
  ],
  "return_transition_columns": [
    103,
    105.5,
    108,
    110.5
  ],
  "q1_in3_vias": 8,
  "branches": {
    "1": {
      "header": "J5",
      "positive_net": "B1_P_RAW",
      "return_net": "POWER_RETURN_JOIN",
      "raw_escape_mm": 21.23336943959638,
      "return_mesh_mm": 89.20156211871642,
      "raw_layers": [
        "F.Cu",
        "B.Cu",
        "In2.Cu"
      ],
      "return_layers": [
        "In1.Cu",
        "In4.Cu"
      ],
      "raw_width_after_pad_mm": 4.0,
      "return_width_mm": 4.0,
      "positive_launch_vias": 24,
      "return_transition_vias": 12,
      "fused_launch_vias": 6,
      "fused_column": 106.5,
      "fuse_xy": [
        36,
        15
      ],
      "source_pad": [
        12.0,
        25
      ],
      "return_pad": [
        12.0,
        30.5
      ],
      "raw_layer_mOhm": 2.6147377795617253,
      "raw_parallel_mOhm": 0.8715792598539084,
      "return_layer_mOhm": 10.984535220904794,
      "return_parallel_mOhm": 5.492267610452397,
      "pad_annulus_mm": 0.4,
      "via_barrel_mOhm_each": 0.19511688667763738,
      "estimated_branch_trace_mOhm": 6.380106610862776
    },
    "2": {
      "header": "J5",
      "positive_net": "B2_P_RAW",
      "return_net": "POWER_RETURN_JOIN",
      "raw_escape_mm": 42.97465680149134,
      "return_mesh_mm": 85.00156211871642,
      "raw_layers": [
        "F.Cu",
        "B.Cu",
        "In2.Cu"
      ],
      "return_layers": [
        "In1.Cu",
        "In4.Cu"
      ],
      "raw_width_after_pad_mm": 4.0,
      "return_width_mm": 4.0,
      "positive_launch_vias": 24,
      "return_transition_vias": 12,
      "fused_launch_vias": 6,
      "fused_column": 109.0,
      "fuse_xy": [
        64,
        15
      ],
      "source_pad": [
        16.2,
        25
      ],
      "return_pad": [
        16.2,
        30.5
      ],
      "raw_layer_mOhm": 5.292022023269362,
      "raw_parallel_mOhm": 1.7640073410897872,
      "return_layer_mOhm": 10.467335220904793,
      "return_parallel_mOhm": 5.233667610452397,
      "pad_annulus_mm": 0.4,
      "via_barrel_mOhm_each": 0.19511688667763738,
      "estimated_branch_trace_mOhm": 7.013934692098654
    },
    "3": {
      "header": "J5",
      "positive_net": "B3_P_RAW",
      "return_net": "POWER_RETURN_JOIN",
      "raw_escape_mm": 66.19347708295602,
      "return_mesh_mm": 80.80156211871642,
      "raw_layers": [
        "F.Cu",
        "B.Cu",
        "In2.Cu"
      ],
      "return_layers": [
        "In1.Cu",
        "In4.Cu"
      ],
      "raw_width_after_pad_mm": 4.0,
      "return_width_mm": 4.0,
      "positive_launch_vias": 24,
      "return_transition_vias": 12,
      "fused_launch_vias": 6,
      "fused_column": 111.5,
      "fuse_xy": [
        92,
        15
      ],
      "source_pad": [
        20.4,
        25
      ],
      "return_pad": [
        20.4,
        30.5
      ],
      "raw_layer_mOhm": 8.151253892215442,
      "raw_parallel_mOhm": 2.7170846307384804,
      "return_layer_mOhm": 9.95013522090479,
      "return_parallel_mOhm": 4.975067610452395,
      "pad_annulus_mm": 0.4,
      "via_barrel_mOhm_each": 0.19511688667763738,
      "estimated_branch_trace_mOhm": 7.7084119817473455
    },
    "4": {
      "header": "J6",
      "positive_net": "B4_P_RAW",
      "return_net": "POWER_RETURN_JOIN",
      "raw_escape_mm": 21.23336943959638,
      "return_mesh_mm": 89.20156211871642,
      "raw_layers": [
        "F.Cu",
        "B.Cu",
        "In2.Cu"
      ],
      "return_layers": [
        "In1.Cu",
        "In4.Cu"
      ],
      "raw_width_after_pad_mm": 4.0,
      "return_width_mm": 4.0,
      "positive_launch_vias": 24,
      "return_transition_vias": 12,
      "fused_launch_vias": 6,
      "fused_column": 104.0,
      "fuse_xy": [
        36,
        40
      ],
      "source_pad": [
        12.0,
        50
      ],
      "return_pad": [
        12.0,
        55.5
      ],
      "raw_layer_mOhm": 2.6147377795617253,
      "raw_parallel_mOhm": 0.8715792598539084,
      "return_layer_mOhm": 10.984535220904794,
      "return_parallel_mOhm": 5.492267610452397,
      "pad_annulus_mm": 0.4,
      "via_barrel_mOhm_each": 0.19511688667763738,
      "estimated_branch_trace_mOhm": 6.380106610862776
    },
    "5": {
      "header": "J6",
      "positive_net": "B5_P_RAW",
      "return_net": "POWER_RETURN_JOIN",
      "raw_escape_mm": 42.97465680149134,
      "return_mesh_mm": 85.00156211871642,
      "raw_layers": [
        "F.Cu",
        "B.Cu",
        "In2.Cu"
      ],
      "return_layers": [
        "In1.Cu",
        "In4.Cu"
      ],
      "raw_width_after_pad_mm": 4.0,
      "return_width_mm": 4.0,
      "positive_launch_vias": 24,
      "return_transition_vias": 12,
      "fused_launch_vias": 6,
      "fused_column": 106.5,
      "fuse_xy": [
        64,
        40
      ],
      "source_pad": [
        16.2,
        50
      ],
      "return_pad": [
        16.2,
        55.5
      ],
      "raw_layer_mOhm": 5.292022023269362,
      "raw_parallel_mOhm": 1.7640073410897872,
      "return_layer_mOhm": 10.467335220904793,
      "return_parallel_mOhm": 5.233667610452397,
      "pad_annulus_mm": 0.4,
      "via_barrel_mOhm_each": 0.19511688667763738,
      "estimated_branch_trace_mOhm": 7.013934692098654
    },
    "6": {
      "header": "J6",
      "positive_net": "B6_P_RAW",
      "return_net": "POWER_RETURN_JOIN",
      "raw_escape_mm": 66.19347708295602,
      "return_mesh_mm": 80.80156211871642,
      "raw_layers": [
        "F.Cu",
        "B.Cu",
        "In2.Cu"
      ],
      "return_layers": [
        "In1.Cu",
        "In4.Cu"
      ],
      "raw_width_after_pad_mm": 4.0,
      "return_width_mm": 4.0,
      "positive_launch_vias": 24,
      "return_transition_vias": 12,
      "fused_launch_vias": 6,
      "fused_column": 109.0,
      "fuse_xy": [
        92,
        40
      ],
      "source_pad": [
        20.4,
        50
      ],
      "return_pad": [
        20.4,
        55.5
      ],
      "raw_layer_mOhm": 8.151253892215442,
      "raw_parallel_mOhm": 2.7170846307384804,
      "return_layer_mOhm": 9.95013522090479,
      "return_parallel_mOhm": 4.975067610452395,
      "pad_annulus_mm": 0.4,
      "via_barrel_mOhm_each": 0.19511688667763738,
      "estimated_branch_trace_mOhm": 7.7084119817473455
    },
    "7": {
      "header": "J9",
      "positive_net": "B7_P_RAW",
      "return_net": "POWER_RETURN_JOIN",
      "raw_escape_mm": 21.23336943959638,
      "return_mesh_mm": 89.20156211871642,
      "raw_layers": [
        "F.Cu",
        "B.Cu",
        "In2.Cu"
      ],
      "return_layers": [
        "In1.Cu",
        "In4.Cu"
      ],
      "raw_width_after_pad_mm": 4.0,
      "return_width_mm": 4.0,
      "positive_launch_vias": 24,
      "return_transition_vias": 12,
      "fused_launch_vias": 6,
      "fused_column": 111.5,
      "fuse_xy": [
        36,
        65
      ],
      "source_pad": [
        12.0,
        75
      ],
      "return_pad": [
        12.0,
        80.5
      ],
      "raw_layer_mOhm": 2.6147377795617253,
      "raw_parallel_mOhm": 0.8715792598539084,
      "return_layer_mOhm": 10.984535220904794,
      "return_parallel_mOhm": 5.492267610452397,
      "pad_annulus_mm": 0.4,
      "via_barrel_mOhm_each": 0.19511688667763738,
      "estimated_branch_trace_mOhm": 6.380106610862776
    },
    "8": {
      "header": "J9",
      "positive_net": "B8_P_RAW",
      "return_net": "POWER_RETURN_JOIN",
      "raw_escape_mm": 42.97465680149134,
      "return_mesh_mm": 85.00156211871642,
      "raw_layers": [
        "F.Cu",
        "B.Cu",
        "In2.Cu"
      ],
      "return_layers": [
        "In1.Cu",
        "In4.Cu"
      ],
      "raw_width_after_pad_mm": 4.0,
      "return_width_mm": 4.0,
      "positive_launch_vias": 24,
      "return_transition_vias": 12,
      "fused_launch_vias": 6,
      "fused_column": 104.0,
      "fuse_xy": [
        64,
        65
      ],
      "source_pad": [
        16.2,
        75
      ],
      "return_pad": [
        16.2,
        80.5
      ],
      "raw_layer_mOhm": 5.292022023269362,
      "raw_parallel_mOhm": 1.7640073410897872,
      "return_layer_mOhm": 10.467335220904793,
      "return_parallel_mOhm": 5.233667610452397,
      "pad_annulus_mm": 0.4,
      "via_barrel_mOhm_each": 0.19511688667763738,
      "estimated_branch_trace_mOhm": 7.013934692098654
    },
    "9": {
      "header": "J9",
      "positive_net": "B9_P_RAW",
      "return_net": "POWER_RETURN_JOIN",
      "raw_escape_mm": 66.19347708295602,
      "return_mesh_mm": 80.80156211871642,
      "raw_layers": [
        "F.Cu",
        "B.Cu",
        "In2.Cu"
      ],
      "return_layers": [
        "In1.Cu",
        "In4.Cu"
      ],
      "raw_width_after_pad_mm": 4.0,
      "return_width_mm": 4.0,
      "positive_launch_vias": 24,
      "return_transition_vias": 12,
      "fused_launch_vias": 6,
      "fused_column": 106.5,
      "fuse_xy": [
        92,
        65
      ],
      "source_pad": [
        20.4,
        75
      ],
      "return_pad": [
        20.4,
        80.5
      ],
      "raw_layer_mOhm": 8.151253892215442,
      "raw_parallel_mOhm": 2.7170846307384804,
      "return_layer_mOhm": 9.95013522090479,
      "return_parallel_mOhm": 4.975067610452395,
      "pad_annulus_mm": 0.4,
      "via_barrel_mOhm_each": 0.19511688667763738,
      "estimated_branch_trace_mOhm": 7.7084119817473455
    }
  },
  "extraction": {
    "rho_ohm_mm2_per_mm": 1.724e-05,
    "copper_thickness_mm": 0.035,
    "via_barrel_mOhm_each": 0.19511688667763738,
    "effective_branch_network_mOhm": 0.7769302822871131,
    "distributed_field_mOhm": 0.12,
    "q1_in3_mOhm": 0.08,
    "pcb_neck_effective_mOhm": 0.9769302822871131,
    "threshold_mOhm": 0.65,
    "status": "TRACE_AND_VIA_MODEL_ONLY_REQUIRES_FAB_STACKUP_THERMAL_VALIDATION"
  },
  "r3_budget": {
    "harness_mOhm": 1.8,
    "fuse_holder_mOhm": 0.55,
    "pcb_neck_network_mOhm": 0.9769302822871131,
    "branch_joins_transitions_mOhm": 0.45,
    "q1_channel_hot_mOhm": 4.32,
    "q1_leads_pads_mOhm": 0.15,
    "protected_copper_j1_mOhm": 0.25,
    "residual_mOhm": 0.08,
    "complete_hot_path_mOhm": 8.576930282287114
  },
  "current_density": {
    "nominal_A": 40,
    "peak_A": 45,
    "raw_pad_bottleneck_A_per_mm2": 519.4805194805194,
    "mesh_4mm_layer_A_per_mm2": 95.23809523809523,
    "status": "THERMAL_MODEL_UNPROVEN"
  },
  "thermal": {
    "status": "UNPROVEN_REQUIRES_PROTOTYPE_VALIDATION",
    "temperature_rise_C": null
  }
}
