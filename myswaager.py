import pymysql

# 資料庫連線設定
DB_CONFIG = {
    "host": "labdb.coded2.fun",
    "user": "dino",
    "password": "1234",
    "database": "DINO",
    "port": 3306,
    "cursorclass": pymysql.cursors.DictCursor  # 使用 DictCursor
}

def fetch_sentiment_scores(date, keyword):
    try:
        # 連線到 MariaDB
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # **獲取單筆 sentiment_score 列表**
        query = """
        SELECT sentiment_score 
        FROM ptt 
        WHERE capture_date = %s AND search_keyword = %s;
        """
        cursor.execute(query, (date, keyword))
        results = cursor.fetchall()

        # 如果沒有數據，回報
        if not results:
            print("\n⚠️ 沒有符合條件的數據 ⚠️")
            return

        # 計算總分
        total = 0.0
        print("\nSentiment Scores:")
        for row in results:
            sentiment_score = float(row['sentiment_score']) if row['sentiment_score'] is not None else 0.0
            print(f"Score: {sentiment_score}")
            total += sentiment_score  # 加總

        return f"\n✅ Total Sentiment Score: {total}"

    except pymysql.MySQLError as e:
        return f"❌ 資料庫錯誤: {e}"

    finally:
        if connection:
            cursor.close()
            connection.close()




