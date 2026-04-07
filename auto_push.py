#!/usr/bin/env python3
"""
Discord德语学习文档自动推送脚本
自动检测文档变化并推送到GitHub
"""

import os
import sys
import time
import logging
from pathlib import Path
from datetime import datetime
import subprocess

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('auto_push.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AutoGitPusher:
    def __init__(self, repo_path):
        self.repo_path = Path(repo_path)
        self.git_exe = "git"
        
    def run_git_command(self, args, cwd=None):
        """运行Git命令（使用cmd解决PowerShell问题）"""
        if cwd is None:
            cwd = self.repo_path
            
        try:
            # 使用cmd执行Git命令，解决PowerShell集成问题
            cmd_args = ['cmd', '/c', self.git_exe] + args
            result = subprocess.run(
                cmd_args,
                cwd=cwd,
                capture_output=True,
                text=True,
                encoding='utf-8',
                timeout=30
            )
            return result.returncode == 0, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            logger.error(f"Git命令超时: {' '.join(args)}")
            return False, "", "命令执行超时"
        except Exception as e:
            logger.error(f"执行Git命令失败: {e}")
            return False, "", str(e)
    
    def check_changes(self):
        """检查是否有未提交的更改"""
        # 检查工作区状态
        success, stdout, stderr = self.run_git_command(["status", "--porcelain"])
        if not success:
            logger.error(f"检查状态失败: {stderr}")
            return False
        
        changes = [line for line in stdout.strip().split('\n') if line]
        return len(changes) > 0
    
    def add_changes(self):
        """添加所有更改到暂存区"""
        success, stdout, stderr = self.run_git_command(["add", "."])
        if success:
            logger.info("已添加所有更改到暂存区")
        else:
            logger.error(f"添加更改失败: {stderr}")
        return success
    
    def commit_changes(self, message=None):
        """提交更改"""
        if message is None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"自动更新: {timestamp}"
        
        success, stdout, stderr = self.run_git_command(["commit", "-m", message])
        if success:
            logger.info(f"提交成功: {message}")
            # 获取提交哈希
            _, hash_stdout, _ = self.run_git_command(["rev-parse", "HEAD"])
            commit_hash = hash_stdout.strip()
            logger.info(f"提交哈希: {commit_hash}")
        else:
            logger.error(f"提交失败: {stderr}")
        
        return success
    
    def push_changes(self):
        """推送到远程仓库"""
        success, stdout, stderr = self.run_git_command(["push", "origin", "master"])
        if success:
            logger.info("推送成功")
        else:
            logger.error(f"推送失败: {stderr}")
            
            # 尝试拉取最新更改后重试
            logger.info("尝试拉取最新更改...")
            pull_success, pull_stdout, pull_stderr = self.run_git_command(["pull", "--rebase"])
            if pull_success:
                logger.info("拉取成功，重新推送...")
                success, stdout, stderr = self.run_git_command(["push", "origin", "master"])
                if success:
                    logger.info("重新推送成功")
        
        return success
    
    def auto_push(self):
        """自动推送流程"""
        logger.info("开始自动推送检查...")
        
        # 1. 检查更改
        if not self.check_changes():
            logger.info("没有检测到更改")
            return False, "没有更改"
        
        logger.info("检测到未提交的更改")
        
        # 2. 添加更改
        if not self.add_changes():
            return False, "添加更改失败"
        
        # 3. 提交更改
        if not self.commit_changes():
            return False, "提交失败"
        
        # 4. 推送更改
        if not self.push_changes():
            return False, "推送失败"
        
        logger.info("自动推送流程完成")
        return True, "推送成功"
    
    def setup_remote(self, remote_url):
        """设置远程仓库"""
        # 检查是否已设置远程仓库
        success, stdout, stderr = self.run_git_command(["remote", "-v"])
        if "origin" in stdout:
            logger.info("远程仓库已设置")
            return True
        
        # 添加远程仓库
        success, stdout, stderr = self.run_git_command(["remote", "add", "origin", remote_url])
        if success:
            logger.info(f"已添加远程仓库: {remote_url}")
        else:
            logger.error(f"添加远程仓库失败: {stderr}")
        
        return success

def main():
    """主函数"""
    # 仓库路径
    repo_path = "C:/Users/men/.openclaw/workspace/deutsch-docs"
    
    # 创建推送器
    pusher = AutoGitPusher(repo_path)
    
    # 运行自动推送
    success, message = pusher.auto_push()
    
    if success:
        print(f"[SUCCESS] {message}")
        return 0
    else:
        print(f"[FAILED] {message}")
        return 1

if __name__ == "__main__":
    sys.exit(main())