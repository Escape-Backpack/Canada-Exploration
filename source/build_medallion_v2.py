"""Build revised Canada v2, retaining the approved shared back."""
from pathlib import Path
import sys, json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"assets/medallion"
sys.path.insert(0,str(OUT))
sys.path.insert(0,str(ROOT/"source"))
import medallion_cad as cad
from revised_medallion_fronts_v2 import FRONTS

def main():
    reference=OUT/"sources/Maple_Leaf_Reference.svg"
    front,trace=FRONTS["Canada"](reference)
    if not front.is_valid or cad.radial_extent(front)>23.01:
        raise ValueError("Invalid front or relief outside safe face")
    trace["reference"]="assets/medallion/sources/Maple_Leaf_Reference.svg"
    report,checks=cad.build_model(OUT,"Canada","v2",front,trace,
        "Canada_Medallion_v2_Preview.png","Yellow relief: revised maple leaf and train")
    files=[OUT/"STL/Canada_Medallion_OnePiece_v2.stl",
        OUT/"STL/Canada_Back_Lettering_Test_1.2mm_v2.stl",
        OUT/"Front_Relief_v2.svg",OUT/"Back_Engraving_v2.svg",
        OUT/"Canada_Medallion_v2_Preview.png",OUT/"geometry_report_v2.json",
        OUT/"mesh_check_v2.json",OUT/"lettering_test_mesh_check_v2.json",
        OUT/"README_v2.md",OUT/"medallion_cad.py",reference,
        ROOT/"source/revised_medallion_fronts_v2.py",
        ROOT/"source/themed_medallion_fronts_v1.py",Path(__file__).resolve()]
    cad.package_files(ROOT,OUT/"Canada_Medallion_Print_Files_v2.zip",files)
    print(json.dumps({"model":"Canada v2","mesh":checks},indent=2))
if __name__=="__main__":main()
