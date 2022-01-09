import os
# 需要将文件放在与工程文件同级的目录下
# 当前文件路径
CUR_PATH = os.path.dirname(os.path.abspath(__file__))
# 工程workSpce路径
WORK_SPCAE = CUR_PATH + "/iOS_d.xcodeproj/" + "project.xcworkspace"
# 工程scheme 可配置其他scheme
NORMAL_SCHEME = "iOS_d"
OTHER_SCHEME = "iOS_dddd"

BASE_PATH = CUR_PATH
ARCHIEVE_TEMP_PATH_DIR = "archieve_temp"
EXPORT_IPA_ROOT_PATH = BASE_PATH + "/" + ARCHIEVE_TEMP_PATH_DIR
EXPORTOPTIONSPLIST_PATH = BASE_PATH + "/exportOptionsPlist.plist"

RELEASE = "Release"
DEBUG = "Debug"




def archieve_target(scheme,build_mode,export_plist_path):
    export_ipa_path = EXPORT_IPA_ROOT_PATH + "/" + scheme
    xcarchieve_path = export_ipa_path + "/" + scheme + ".xcarchive"
    os.mkdir(export_ipa_path)


    print("====={scheme}_action_start=====".format(scheme=scheme))
    clean_work_cmd = "xcodebuild clean -workspace {workspace_path}  -scheme {app_scheme}  -configuration {build_mode}".format(workspace_path=WORK_SPCAE,app_scheme=scheme,build_mode=build_mode)
    os.system(clean_work_cmd)
    print("====={scheme}_clean_end=====".format(scheme=scheme));
    build_work_cmd = "xcodebuild archive -workspace {workspace_path} -scheme {app_scheme} -configuration {build_mode} -archivePath {xcarchive_path}".format(workspace_path=WORK_SPCAE,app_scheme=scheme,build_mode=build_mode,xcarchive_path=xcarchieve_path)
    os.system(build_work_cmd)
    print("====={scheme}_build_end=====".format(scheme=scheme))
    export_archive_cmd = "xcodebuild -exportArchive -archivePath {xcarchive_path} -exportPath {export_ipa_path} -exportOptionsPlist {exportOptionsPlist_path}".format(xcarchive_path=xcarchieve_path,export_ipa_path=export_ipa_path,exportOptionsPlist_path=export_plist_path)
    os.system(export_archive_cmd)
    print("====={scheme}_action_end=====".format(scheme=scheme))




if __name__ == '__main__':


    if os.path.exists(EXPORT_IPA_ROOT_PATH):
        for root, dirs, files in os.walk(EXPORT_IPA_ROOT_PATH, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(EXPORT_IPA_ROOT_PATH)

    os.mkdir(EXPORT_IPA_ROOT_PATH)

    # 执行打包针对Scheme
    archieve_target(NORMAL_SCHEME,RELEASE,EXPORTOPTIONSPLIST_PATH)
    archieve_target(OTHER_SCHEME,RELEASE,EXPORTOPTIONSPLIST_PATH)


