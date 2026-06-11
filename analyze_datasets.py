import os
import time
import numpy as np
import scipy.ndimage as ndimage
from PIL import Image

def format_number(val):
    if val >= 1000000:
        return f"{val/1000000:.1f}M".replace(".0M", "M")
    elif val >= 1000:
        return f"{val/1000:.1f}K".replace(".0K", "K")
    else:
        return str(val)

def extract_objects_from_image(img_path, is_binary):
    try:
        img = Image.open(img_path)
        arr = np.array(img)
    except Exception as e:
        print(f"Error reading {img_path}: {e}")
        return []

    objects = []
    if is_binary:
        # Binary mask (0 and 255/1). Find connected components.
        labeled_arr, num_features = ndimage.label(arr > 0)
        areas = np.bincount(labeled_arr.ravel())
        slices = ndimage.find_objects(labeled_arr)
        
        for idx, sl in enumerate(slices):
            if sl is None:
                continue
            val = idx + 1
            area = areas[val]
            if area <= 2:  # Skip tiny noise
                continue
            h = sl[0].stop - sl[0].start
            w = sl[1].stop - sl[1].start
            objects.append({
                'area': area,
                'w': w,
                'h': h
            })
    else:
        # Labeled instance mask (0 is background, positive integers are unique instances).
        areas = np.bincount(arr.ravel())
        slices = ndimage.find_objects(arr)
        
        for idx, sl in enumerate(slices):
            if sl is None:
                continue
            val = idx + 1
            area = areas[val]
            if area <= 2:  # Skip tiny noise
                continue
            h = sl[0].stop - sl[0].start
            w = sl[1].stop - sl[1].start
            objects.append({
                'area': area,
                'w': w,
                'h': h
            })
            
    return objects

def analyze_subfolder(subfolder_path, is_binary):
    if not os.path.exists(subfolder_path):
        return None
    
    files = sorted([f for f in os.listdir(subfolder_path) if f.endswith(('.tif', '.png'))])
    if not files:
        return None
    
    all_objects = []
    for f in files:
        img_path = os.path.join(subfolder_path, f)
        objs = extract_objects_from_image(img_path, is_binary)
        all_objects.extend(objs)
        
    return len(files), all_objects

def main():
    archive_dir = "/Users/phamngoctu/Documents/YOLO instance segmentation/archive"
    
    subfolders_to_analyze = [
        ("label masks", False),
        ("label masks modify", False),
        ("mask binary", True),
        ("mask binary without border", True),
        ("mask binary without border erode", True)
    ]
    
    results = []
    
    print("Starting dataset analysis...")
    t_start = time.time()
    
    body_parts = sorted([d for d in os.listdir(archive_dir) if os.path.isdir(os.path.join(archive_dir, d))])
    
    for part in body_parts:
        part_path = os.path.join(archive_dir, part)
        print(f"Processing: {part}...")
        
        for sub_name, is_binary in subfolders_to_analyze:
            sub_path = os.path.join(part_path, sub_name)
            res = analyze_subfolder(sub_path, is_binary)
            if res is None:
                continue
            
            num_images, objects = res
            
            # Categorize into bins
            # Method A: Area-based
            area_small = 0
            area_medium = 0
            area_large = 0
            
            # Method B: BBox dimension-based
            bbox_small = 0
            bbox_medium = 0
            bbox_large = 0
            
            for obj in objects:
                # Area-based binning (equivalent diameter / sqrt(area) < 32, 32-96, >96)
                area = obj['area']
                if area < 1024:
                    area_small += 1
                elif area <= 9216:
                    area_medium += 1
                else:
                    area_large += 1
                    
                # BBox dimension-based binning (max(w, h) < 32, 32-96, >96)
                size_max = max(obj['w'], obj['h'])
                if size_max < 32:
                    bbox_small += 1
                elif size_max <= 96:
                    bbox_medium += 1
                else:
                    bbox_large += 1
            
            results.append({
                'body_part': part,
                'subfolder': sub_name,
                'num_images': num_images,
                'area_small': area_small,
                'area_medium': area_medium,
                'area_large': area_large,
                'bbox_small': bbox_small,
                'bbox_medium': bbox_medium,
                'bbox_large': bbox_large
            })
            
    t_end = time.time()
    print(f"Analysis completed in {t_end - t_start:.2f} seconds.")
    
    # Helper to build a markdown table for a given metric and subfolder name
    def build_table(sub_name, is_bbox_method):
        table_lines = [
            f"### Subfolder: `{sub_name}`",
            "",
            "| Body Part | Small (<32px) | Medium (32–96px) | Large (>96px) | Total |",
            "| :--- | :--- | :--- | :--- | :--- |"
        ]
        
        filtered = [r for r in results if r['subfolder'] == sub_name]
        
        sum_small = 0
        sum_medium = 0
        sum_large = 0
        
        for r in filtered:
            if is_bbox_method:
                s, m, l = r['bbox_small'], r['bbox_medium'], r['bbox_large']
            else:
                s, m, l = r['area_small'], r['area_medium'], r['area_large']
                
            tot = s + m + l
            sum_small += s
            sum_medium += m
            sum_large += l
            
            table_lines.append(
                f"| {r['body_part']} | {format_number(s)} | {format_number(m)} | {format_number(l)} | {format_number(tot)} |"
            )
            
        sum_tot = sum_small + sum_medium + sum_large
        table_lines.append(
            f"| **Total (Archive)** | **{format_number(sum_small)}** | **{format_number(sum_medium)}** | **{format_number(sum_large)}** | **{format_number(sum_tot)}** |"
        )
        table_lines.append("")
        return "\n".join(table_lines)
        
    # Build sections
    bbox_sections = []
    area_sections = []
    
    for sub_name, _ in subfolders_to_analyze:
        bbox_sections.append(build_table(sub_name, is_bbox_method=True))
        area_sections.append(build_table(sub_name, is_bbox_method=False))
        
    bbox_report_str = "\n".join(bbox_sections)
    area_report_str = "\n".join(area_sections)
    
    # Write to Markdown file
    output_content = f"""# YOLO Instance Segmentation Dataset Analysis Report

This report contains the object size analysis for each subset in the `archive/` directory. Bins are calculated based on two definitions: Bounding Box Dimension and Area (equivalent square side length).

---

## Part 1: Bounding Box Dimension-based Binning
*Bins are defined using the maximum bounding box side length: $\\max(W, H)$ of each object.*
* **Small**: $\\max(W, H) < 32\\text{{ px}}$
* **Medium**: $32\\text{{ px}} \\le \\max(W, H) \\le 96\\text{{ px}}$
* **Large**: $\\max(W, H) > 96\\text{{ px}}$

{bbox_report_str}

---

## Part 2: Area-based Binning (Equivalent Square Side Length)
*Bins are defined using the object's mask area (pixel count):*
* **Small**: $\\text{{area}} < 1024\\text{{ px}}^2$ ($32^2$)
* **Medium**: $1024\\text{{ px}}^2 \\le \\text{{area}} \\le 9216\\text{{ px}}^2$ (between $32^2$ and $96^2$)
* **Large**: $\\text{{area}} > 9216\\text{{ px}}^2$ ($96^2$)

{area_report_str}
"""
    
    # Save files
    workspace_out = "/Users/phamngoctu/Documents/YOLO instance segmentation/dataset_analysis.md"
    artifact_out = "/Users/phamngoctu/.gemini/antigravity-ide/brain/d926dfa1-9808-42ab-bb6b-71754e391a1b/dataset_analysis.md"
    
    with open(workspace_out, "w") as f:
        f.write(output_content)
    with open(artifact_out, "w") as f:
        f.write(output_content)
        
    print(f"Report saved to:\n  - {workspace_out}\n  - {artifact_out}")

if __name__ == "__main__":
    main()
