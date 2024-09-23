import os
import subprocess

def deploy():
    # Use a path within the GitHub workspace
    deploy_path = os.path.join(os.environ.get('GITHUB_WORKSPACE', ''), 'deploy_output')

    # Create the deployment directory if it doesn't exist
    os.makedirs(deploy_path, exist_ok=True)

    # Copy the add.py script to the deployment directory
    subprocess.run(["cp", "add.py", deploy_path])

    print(f"Deployed add.py to {deploy_path}")

    # Optional: Run the script to test it
    print("Testing the deployed script:")
    result = subprocess.run(["python", os.path.join(deploy_path, "add.py")], 
                            input="5\n3\n", 
                            text=True, 
                            capture_output=True)
    
    print(result.stdout)

if __name__ == "__main__":
    deploy()