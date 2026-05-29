import os


def createfile(filepath):
    if not os.path.exists(filepath):
        file = open(filepath, "w")
        file.close()


class Pvcs:
    #디렉토리 위치 설정
    def __init__(self):
        self.HISTDIR = ".pvcshist" #옛 코밋 저장하는 위치
        self.CONFIGDIR = ".pvcsconfig" #추적하는 파일
        self.IGNOREDIR = ".pvcsignore" #무시할 파일

    #리포 초기화
    def init_repo(self):
        if not os.path.exists(self.HISTDIR):
            os.makedirs(self.HISTDIR)

    def load_from_file(self, filepath, index):
        if not os.path.exists(filepath):
            return []
        else:
            with open(filepath, "r") as file:
                for line in file:
                    if index in line:
                return None