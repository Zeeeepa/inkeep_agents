#!/usr/bin/env python3
"""
Automated CI/CD Compatibility Analysis for All Repos
Creates parallel agent runs to analyze each repository
"""

import json
import os
import sys
from codegen import Codegen

def create_analysis_agents():
    """Create agent runs for all repositories"""
    
    # Load repos
    with open('all_repos.json', 'r') as f:
        repos = json.load(f)
    
    print(f"📊 Total repositories to analyze: {len(repos)}")
    
    # Initialize Codegen client
    client = Codegen()
    
    branch_name = "cicd-ratings"
    
    # Analysis prompt template
    prompt_template = """Analyze the repository '{repo_name}' for enterprise CI/CD compatibility.

**Task:**
1. Set active codebase to {repo_name}
2. Run repomix to generate full analysis
3. Read repomix output
4. Rate the repository (0-10) based on these criteria:
   - Build System (0-2): Modern tools, reproducible builds, dependency mgmt
   - Testing (0-2): Unit tests, test framework, CI automation ready  
   - CI/CD Config (0-2): GH Actions/GitLab CI present, workflows, pipelines
   - Documentation (0-1): README, API docs, architecture
   - Code Quality (0-1): Linting, formatting, static analysis
   - Containerization (0-1): Dockerfile, Docker Compose, K8s
   - Security (0-1): Dependency scanning, secrets mgmt, best practices

5. Create rating JSON in this exact format:
```json
{{
  "repo": "{repo_name}",
  "overall_rating": X.X,
  "build_system": X,
  "testing": X,
  "cicd_config": X,
  "documentation": X,
  "code_quality": X,
  "containerization": X,
  "security": X,
  "notes": "Brief analysis",
  "recommendation": "production-ready|needs-work|prototype"
}}
```

6. Append this rating to 'cicd_ratings.json' file (create if doesn't exist)
7. Commit to branch '{branch_name}' with message "Add CI/CD rating for {repo_name}"
8. Push changes

**Important:** 
- Be concise but thorough
- Focus on facts from repomix analysis
- Provide actionable recommendations
"""

    created_count = 0
    failed_count = 0
    
    for idx, repo in enumerate(repos, 1):
        repo_name = repo['name']
        
        try:
            print(f"[{idx}/{len(repos)}] Creating agent for: {repo_name}")
            
            # Create agent run
            prompt = prompt_template.format(
                repo_name=repo_name,
                branch_name=branch_name
            )
            
            # Use Codegen SDK to create agent run
            # (Replace with actual SDK method - this is pseudo-code)
            run = client.create_agent_run(
                repo=f"Zeeeepa/{repo_name}",
                message=prompt,
                branch=branch_name
            )
            
            created_count += 1
            print(f"  ✅ Created agent run ID: {run.id}")
            
        except Exception as e:
            failed_count += 1
            print(f"  ❌ Failed: {e}")
    
    print(f"\n{'='*60}")
    print(f"✅ Successfully created: {created_count} agent runs")
    print(f"❌ Failed: {failed_count}")
    print(f"⏱️  Estimated completion: ~{len(repos) * 2 / 60:.1f} minutes")
    print(f"{'='*60}")

if __name__ == "__main__":
    create_analysis_agents()
