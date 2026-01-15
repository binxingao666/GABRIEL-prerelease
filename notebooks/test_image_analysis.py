#!/usr/bin/env python3
"""
Test script for GABRIEL image analysis functionality.
Run from the notebooks directory.
"""

import os
import sys
import asyncio
import pandas as pd
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.abspath('../src'))

# Set API credentials
# Set your API credentials here
os.environ["AZURE_OPENAI_API_KEY"] = "YOUR_KEY_HERE"
os.environ["AZURE_OPENAI_ENDPOINT"] = "YOUR_ENDPOINT_HERE"

import gabriel

# Output directory
output_dir = "test_image_output"
os.makedirs(output_dir, exist_ok=True)


async def test_extract():
    """Test A: Extract information from images"""
    print("\n" + "="*60)
    print("TEST A: gabriel.extract() with images")
    print("="*60)

    image_dir = Path("../examples/images")
    image_files = sorted(image_dir.glob("*.jpg"))

    print(f"Found {len(image_files)} images:")
    for img in image_files:
        abs_path = str(img.resolve())
        print(f"  {img.name}: exists={os.path.exists(abs_path)}")

    df_images = pd.DataFrame({
        "image_id": [f"img_{i}" for i in range(len(image_files))],
        "image_path": [str(p.resolve()) for p in image_files],
        "filename": [p.name for p in image_files]
    })

    extracted = await gabriel.extract(
        df=df_images,
        column_name="image_path",
        attributes={
            "product_type": "What type of product is shown? (e.g., watch, shoe, electronics)",
            "primary_color": "What is the dominant color of the product?",
            "background_color": "What is the background color? (e.g., white, gradient, colored)",
        },
        modality="image",
        save_dir=f"{output_dir}/extraction",
        model="gpt-5.2",
        reset_files=True,
    )

    print("\nExtraction Results:")
    display_cols = ["filename", "product_type", "primary_color", "background_color"]
    print(extracted[display_cols].to_string())

    # Check for unknown values
    unknown_count = (extracted[["product_type", "primary_color", "background_color"]] == "unknown").sum().sum()
    print(f"\nUnknown values: {unknown_count}")

    return extracted


async def test_rate():
    """Test B: Rate images on visual attributes"""
    print("\n" + "="*60)
    print("TEST B: gabriel.rate() with images")
    print("="*60)

    image_dir = Path("../examples/images")
    image_files = sorted(image_dir.glob("*.jpg"))

    df_images = pd.DataFrame({
        "image_id": [f"img_{i}" for i in range(len(image_files))],
        "image_path": [str(p.resolve()) for p in image_files],
        "filename": [p.name for p in image_files]
    })

    ratings = await gabriel.rate(
        df=df_images,
        column_name="image_path",
        attributes={
            "visual_appeal": "How visually appealing is this product image? (100 = stunning, 0 = unappealing)",
            "professionalism": "How professional does the product photography look? (100 = studio quality, 0 = amateur)",
        },
        modality="image",
        save_dir=f"{output_dir}/ratings",
        model="gpt-5.2",
        reset_files=True,
    )

    print("\nRating Results:")
    rating_cols = ["filename", "visual_appeal", "professionalism"]
    print(ratings[rating_cols].to_string())

    return ratings


async def test_classify():
    """Test C: Classify images into categories"""
    print("\n" + "="*60)
    print("TEST C: gabriel.classify() with images")
    print("="*60)

    image_dir = Path("../examples/images")
    image_files = sorted(image_dir.glob("*.jpg"))

    df_images = pd.DataFrame({
        "image_id": [f"img_{i}" for i in range(len(image_files))],
        "image_path": [str(p.resolve()) for p in image_files],
        "filename": [p.name for p in image_files]
    })

    # gabriel.classify uses 'labels' parameter, not 'attributes'
    classified = await gabriel.classify(
        df=df_images,
        column_name="image_path",
        labels={
            "is_footwear": "The product is a type of footwear (shoes, sneakers, boots, etc.)",
            "is_electronics": "The product is electronics (headphones, phone, etc.)",
            "is_accessory": "The product is a fashion accessory (watch, sunglasses, etc.)",
        },
        modality="image",
        save_dir=f"{output_dir}/classification",
        model="gpt-5.2",
        reset_files=True,
    )

    print("\nClassification Results:")
    class_cols = ["filename", "is_footwear", "is_electronics", "is_accessory"]
    print(classified[class_cols].to_string())

    return classified


async def test_compare():
    """Test D: Compare two images"""
    print("\n" + "="*60)
    print("TEST D: gabriel.compare() with images")
    print("="*60)

    image_dir = Path("../examples/images")
    image_files = sorted(image_dir.glob("*.jpg"))
    image_paths = [str(p.resolve()) for p in image_files]

    # Find shoe and sneaker
    shoe_path = [p for p in image_paths if "shoe" in p][0]
    sneaker_path = [p for p in image_paths if "sneaker" in p][0]

    print(f"Comparing:")
    print(f"  Circle (shoe): {Path(shoe_path).name}")
    print(f"  Square (sneaker): {Path(sneaker_path).name}")

    df_compare = pd.DataFrame({
        "comparison_id": ["footwear_comparison"],
        "circle_image": [shoe_path],
        "square_image": [sneaker_path]
    })

    # gabriel.compare uses circle_column_name and square_column_name
    # It returns differences, not attribute comparisons
    comparison = await gabriel.compare(
        df=df_compare,
        circle_column_name="circle_image",
        square_column_name="square_image",
        modality="image",
        save_dir=f"{output_dir}/comparison",
        model="gpt-5.2",
        reset_files=True,
    )

    print("\nComparison Results:")
    print(comparison.to_string())

    return comparison


async def main():
    print("GABRIEL Image Analysis Test Script")
    print("="*60)

    # Verify images exist
    image_dir = Path("../examples/images")
    if not image_dir.exists():
        print(f"ERROR: Image directory not found: {image_dir.resolve()}")
        return

    image_files = list(image_dir.glob("*.jpg"))
    if len(image_files) == 0:
        print(f"ERROR: No .jpg files found in {image_dir.resolve()}")
        return

    print(f"Working directory: {os.getcwd()}")
    print(f"Image directory: {image_dir.resolve()}")
    print(f"Images found: {len(image_files)}")

    # Run tests
    try:
        await test_extract()
        await test_rate()
        await test_classify()
        await test_compare()

        print("\n" + "="*60)
        print("ALL TESTS COMPLETED SUCCESSFULLY!")
        print("="*60)

    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
