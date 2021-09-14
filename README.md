# apls

**The implementation of APLS**

APLS is Average Path Length Similarity, which is the evaluation metric for the continuouness of recognized linear spatial objects.

The detailed introduction of APLS is in:

https://medium.com/the-downlinq/spacenet-road-detection-and-routing-challenge-part-ii-apls-implementation-92acd86f4094

https://medium.com/the-downlinq/spacenet-road-detection-and-routing-challenge-part-i-d4f59d55bfce


**Required library**
python 3.6, osgeo, networkx

**The running command**

** # Compare a ground truth geojson with a proposal json

python apls.py --test_method=gt_json_prop_json --output_name=gt_json_prop_json \
	--truth_dir=data/gt_json_prop_json/AOI_2_Vegas_Train/spacenetroads \
	--prop_dir=data/gt_json_prop_json/AOI_2_Vegas_Train/osm 
