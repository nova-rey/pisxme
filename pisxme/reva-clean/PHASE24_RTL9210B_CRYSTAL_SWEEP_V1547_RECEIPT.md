# RTL9210B crystal source sweep receipt — V1547

Date: 2026-09-10

V1547 generated and natively checked 16 saved-board candidates from the
V1523 accepted RTL_3V3 field. It swept XTAL_OUT F.Cu spine positions 90.6,
91.0, 91.4, and 91.8 mm and XTAL_IN transition positions 92.0, 92.4, 92.6,
and 92.8 mm. No synthetic edges or rule changes were used.

The best class is XTAL_OUT at x=91.4 mm with XTAL_IN's B.Cu middle section;
all four variants retain one native clearance violation at the adjacent
XTAL_OUT source track. The sweep therefore rules out scalar endpoint tuning
under the current source geometry. The next class must coauthor a different
source departure/layer allocation. Path A and production CAD are unchanged.
