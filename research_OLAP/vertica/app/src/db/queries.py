import enum


class Queries(enum.Enum):
    create_table = """CREATE TABLE IF NOT EXISTS views (
                            id IDENTITY,
                            user_id VARCHAR(256) NOT NULL,
                            movie_id VARCHAR(256) NOT NULL,
                            viewed_frame INTEGER NOT NULL)"""
    create_start_data = """COPY views(user_id, movie_id, viewed_frame) 
                           FROM '/fish_data.csv' DELIMITER ','"""
    insert_many = """INSERT INTO views (
                            user_id,
                            movie_id,
                            viewed_frame) 
                      VALUES (?, ?, ?);"""
    count_data = """SELECT COUNT(*)
                    from views"""
    avg_data = """SELECT AVG(viewed_frame)
                  from views"""
    get_all = """SELECT * 
                 from views"""
