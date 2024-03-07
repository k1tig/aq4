plant_tag_list = ["ludwigia supered", "lobelia cardinalis", "blyca japonica", "eleocharis mini", "glossostigma elatinoides",]



def TagFilter(tag_type, tag_name):
    tag_obj = []
    if tag_type == "plant":
        for i in plant_tag_list:
            if i == tag_name:
                tag_obj.append(i)


    