import sqlite3
from src.global_src.global_path import ticket_database_path

def get_pixel_art_welcome_msg(ticket_id):
    conn = sqlite3.connect(ticket_database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT welcome_msg_id, channel_id FROM pixel_art WHERE ticket_id = ? AND close_time IS NULL', (ticket_id,))
    welcome_msg_id, channel_id = cursor.fetchone()
    conn.close()
    return welcome_msg_id, channel_id

def get_pixel_art_ticket_open_user_id(ticket_id):
    conn = sqlite3.connect(ticket_database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT open_user_id FROM pixel_art WHERE ticket_id = ? AND close_time IS NULL', (ticket_id,))
    fetch_result = cursor.fetchone()
    conn.close()
    if fetch_result is not None:
        open_user_id = fetch_result[0]
        return open_user_id
    else:
        return None

def check_open_pixel_art_ticket(user_id):
    conn = sqlite3.connect(ticket_database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT ticket_id, channel_id FROM pixel_art WHERE open_user_id = ? AND close_time IS NULL', (user_id,))
    fetch_result = cursor.fetchone()
    conn.close()
    if fetch_result is not None:
        ticket_id, channel_id = fetch_result
        return ticket_id, channel_id
    else:
        return False

def check_claimed_pixeL_art_ticket(ticket_id):
    conn = sqlite3.connect(ticket_database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT claim_user_id FROM pixel_art WHERE ticket_id = ? AND close_time IS NULL', (ticket_id,))
    fetch_result = cursor.fetchone()
    conn.close()
    if fetch_result is not None:
        claimed_users_id = fetch_result[0]
        return claimed_users_id
    else:
        return None

def get_pixel_art_channel_id(ticket_id):
    conn = sqlite3.connect(ticket_database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT channel_id FROM pixel_art WHERE ticket_id = ?', (ticket_id,))
    fetch_result = cursor.fetchone()
    conn.close()
    if fetch_result is not None:
        channel_id = fetch_result[0]
        return channel_id
    else:
        return None

def get_pixel_art_queue_message_id(ticket_id):
    conn = sqlite3.connect(ticket_database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT queue_msg_id FROM pixel_art WHERE ticket_id = ?', (ticket_id,))
    fetch_result = cursor.fetchone()
    conn.close()
    if fetch_result is not None:
        queue_msg_id = fetch_result[0]
        return queue_msg_id
    else:
        return None

def get_pixel_art_log_message_id(ticket_id):
    conn = sqlite3.connect(ticket_database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT log_msg_id FROM pixel_art WHERE ticket_id = ?', (ticket_id,))
    fetch_result = cursor.fetchone()
    conn.close()
    if fetch_result is not None:
        queue_msg_id = fetch_result[0]
        return queue_msg_id
    else:
        return None

def get_pixel_art_dm_message_id(ticket_id):
    conn = sqlite3.connect(ticket_database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT open_user_id, dm_msg_id FROM pixel_art WHERE ticket_id = ?', (ticket_id,))
    fetch_result = cursor.fetchone()
    conn.close()
    if fetch_result is not None:
        open_user_id = fetch_result[0]
        dm_msg_id = fetch_result[1]
        return open_user_id, dm_msg_id
    else:
        return None

def get_pixel_art_confirm_message_id(ticket_id):
    conn = sqlite3.connect(ticket_database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT confirm_message_id FROM pixel_art WHERE ticket_id = ?', (ticket_id,))
    fetch_result = cursor.fetchone()
    conn.close()
    if fetch_result is not None:
        confirm_message_id = fetch_result[0]
        return confirm_message_id
    else:
        return None