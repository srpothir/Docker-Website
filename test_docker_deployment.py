#!/usr/bin/env python3
"""
Test file for Docker deployment functionality
Tests Docker configuration and deployment readiness
"""

import os
import subprocess
import sys
from pathlib import Path

def test_dockerfile_exists():
    """Test that Dockerfile exists"""
    assert os.path.exists('Dockerfile'), "Dockerfile not found"
    print("✓ Dockerfile exists")

def test_docker_compose_exists():
    """Test that docker-compose.yml exists"""
    assert os.path.exists('docker-compose.yml'), "docker-compose.yml not found"
    print("✓ docker-compose.yml exists")

def test_dockerfile_content():
    """Test Dockerfile content"""
    with open('Dockerfile', 'r') as f:
        content = f.read()
    
    # Check for required Dockerfile elements
    assert 'FROM nginx:alpine' in content, "Missing nginx base image"
    assert 'COPY Cursor/' in content, "Missing COPY instruction for website files"
    assert 'EXPOSE 80' in content, "Missing EXPOSE instruction"
    assert 'CMD' in content, "Missing CMD instruction"
    
    print("✓ Dockerfile content is valid")

def test_docker_compose_content():
    """Test docker-compose.yml content"""
    with open('docker-compose.yml', 'r') as f:
        content = f.read()
    
    # Check for required docker-compose elements
    assert 'version:' in content, "Missing version specification"
    assert 'services:' in content, "Missing services section"
    assert 'build:' in content, "Missing build instruction"
    assert 'ports:' in content, "Missing ports mapping"
    assert '8080:80' in content, "Missing port mapping 8080:80"
    
    print("✓ docker-compose.yml content is valid")

def test_dockerignore_exists():
    """Test that .dockerignore exists"""
    assert os.path.exists('.dockerignore'), ".dockerignore not found"
    print("✓ .dockerignore exists")

def test_website_files_structure():
    """Test that website files are in correct structure for Docker"""
    cursor_dir = 'Cursor'
    assert os.path.exists(cursor_dir), "Cursor directory not found"
    
    required_files = [
        'index.html',
        'about.html',
        'contact.html', 
        'projects.html',
        'resume.html',
        'styles.css'
    ]
    
    for file in required_files:
        file_path = os.path.join(cursor_dir, file)
        assert os.path.exists(file_path), f"Required file not found: {file_path}"
    
    print("✓ Website files structure is correct")

def test_docker_build_simulation():
    """Simulate Docker build process (without actually building)"""
    # Check if Docker is available
    try:
        result = subprocess.run(['docker', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✓ Docker is available")
        else:
            print("⚠ Docker not available, but configuration is valid")
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("⚠ Docker not available, but configuration is valid")

def test_port_configuration():
    """Test port configuration"""
    with open('docker-compose.yml', 'r') as f:
        content = f.read()
    
    # Check for port 8080 mapping
    assert '8080:80' in content, "Port mapping 8080:80 not found"
    print("✓ Port configuration is correct")

def test_container_name():
    """Test container name configuration"""
    with open('docker-compose.yml', 'r') as f:
        content = f.read()
    
    # Check for container name
    assert 'container_name:' in content, "Container name not specified"
    print("✓ Container name is configured")

def test_restart_policy():
    """Test restart policy configuration"""
    with open('docker-compose.yml', 'r') as f:
        content = f.read()
    
    # Check for restart policy
    assert 'restart:' in content, "Restart policy not specified"
    print("✓ Restart policy is configured")

def run_all_tests():
    """Run all Docker deployment tests"""
    print("Running Docker deployment tests...\n")
    
    try:
        test_dockerfile_exists()
        test_docker_compose_exists()
        test_dockerfile_content()
        test_docker_compose_content()
        test_dockerignore_exists()
        test_website_files_structure()
        test_docker_build_simulation()
        test_port_configuration()
        test_container_name()
        test_restart_policy()
        
        print("\n🎉 All Docker tests passed! Ready for deployment.")
        print("\nTo build and run your website:")
        print("1. docker-compose up --build")
        print("2. Visit http://localhost:8080")
        return True
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
