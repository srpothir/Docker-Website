#!/usr/bin/env python3
"""
Test file for personal website functionality
Tests basic HTML structure and content validation
"""

import os
import re
from pathlib import Path

def test_html_files_exist():
    """Test that all required HTML files exist"""
    required_files = [
        'Cursor/index.html',
        'Cursor/about.html', 
        'Cursor/contact.html',
        'Cursor/projects.html',
        'Cursor/resume.html',
        'Cursor/thankyou.html'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    assert len(missing_files) == 0, f"Missing files: {missing_files}"
    print("✓ All required HTML files exist")

def test_css_file_exists():
    """Test that CSS file exists"""
    css_path = 'Cursor/styles.css'
    assert os.path.exists(css_path), f"CSS file not found: {css_path}"
    print("✓ CSS file exists")

def test_images_directory():
    """Test that images directory exists and contains files"""
    images_dir = 'Cursor/images'
    assert os.path.exists(images_dir), f"Images directory not found: {images_dir}"
    
    image_files = os.listdir(images_dir)
    assert len(image_files) > 0, "Images directory is empty"
    print(f"✓ Images directory exists with {len(image_files)} files")

def test_html_structure():
    """Test basic HTML structure in index.html"""
    with open('Cursor/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for basic HTML structure
    assert '<!DOCTYPE html>' in content, "Missing DOCTYPE declaration"
    assert '<html lang="en">' in content, "Missing html tag with lang attribute"
    assert '<head>' in content, "Missing head tag"
    assert '<body>' in content, "Missing body tag"
    assert '</html>' in content, "Missing closing html tag"
    
    print("✓ HTML structure is valid")

def test_navigation_links():
    """Test that navigation links are present"""
    with open('Cursor/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for navigation links
    nav_links = ['about.html', 'resume.html', 'projects.html', 'contact.html']
    for link in nav_links:
        assert link in content, f"Navigation link {link} not found"
    
    print("✓ Navigation links are present")

def test_css_link():
    """Test that CSS file is linked"""
    with open('Cursor/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    assert 'styles.css' in content, "CSS file not linked"
    print("✓ CSS file is linked")

def test_responsive_design():
    """Test for responsive design elements"""
    with open('Cursor/styles.css', 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Check for media queries
    assert '@media' in css_content, "No media queries found for responsive design"
    print("✓ Responsive design elements found")

def test_contact_form():
    """Test contact form structure"""
    with open('Cursor/contact.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for form elements
    assert '<form' in content, "No form element found"
    assert 'input' in content, "No input elements found"
    assert 'textarea' in content, "No textarea element found"
    
    print("✓ Contact form structure is valid")

def run_all_tests():
    """Run all tests"""
    print("Running website functionality tests...\n")
    
    try:
        test_html_files_exist()
        test_css_file_exists()
        test_images_directory()
        test_html_structure()
        test_navigation_links()
        test_css_link()
        test_responsive_design()
        test_contact_form()
        
        print("\n[SUCCESS] All tests passed! Website is ready for deployment.")
        return True
        
    except AssertionError as e:
        print(f"\n[ERROR] Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
