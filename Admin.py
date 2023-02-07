import TJ_DBConnection

conn, cursor, result = TJ_DBConnection.dbconn()

class adminList:
    # 관리자 기능 검색
    def searchComment(comment):
        managing_list = ["인사", "유저", "채팅기록", "음성기록"]
        function_list = ["인원정리"]
        try:
            if comment in managing_list:
                print("channel")
        except:
            return 0
    
    # 관리자 기능: 인사
    def helloBot(comment):
        return "hello"
        # return channel.send("Hello! "+str(user))
        
    # 관리자 기능: 유저
    # 관리자 기능: 채팅기록
    # 관리자 기능: 음성기록