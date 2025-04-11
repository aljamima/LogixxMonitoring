#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from flask import Flask, render_template
from flask_sqlalchemy import _QueryProperty, SQLAlchemy
#import MySQLdb
import mysql.connector
#from flask import g
from flask import Flask, g, request
import flask
import logging 
from flask import current_app
from datetime import datetime as dt
now = dt.now()
from mysql.connector import errorcode


log_file = 'test.log'


#hash_unit=hash_unit, site_name=site_name, users=data, total_hashrate=total_hashrate.replace("(","").replace(")",""), on_off=on_off, temp_av=temp_av, card_count=card_count 
hash_unit = 'Gh'
site_name = ''
data = ''
total_hashrate = ''
on_off = ''
temp_av = ''
card_count = ''


@blueprint.route('/index')
@login_required
def index():
    global hash_unit, site_name, data, total_hashrate, on_off, temp_av, card_count
    handler = logging.FileHandler("test.log")  # Create the file logger
    current_app.logger.addHandler(handler)
    current_app.logger.setLevel(logging.DEBUG)         # Set the log level to debug
    current_app.logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
    current_app.logger.info('getting index page')
    current_app.logger.info('route: ' + str(request.access_route) + 'blueprint: ' + str(request.blueprints) + 'cookies: ' + str(request.cookies) + 'full path' + str(request.full_path) + 'user_agent: ' + str(request.user_agent) + 'remote_addr: ' + str(request.remote_addr))

    try:
        #user = User.query
        miner_db = "quincy_miners"
        conn = mysql.connector.connect (
            host="192.168.222.13",
            user="shawnm",
            port="3306",
            password="Gr33nDr34m5!@#",
            database=miner_db,
            auth_plugin='mysql_native_password', )
        conn.autocommit = True
        cursor = conn.cursor() 
        cursor.execute("SELECT SUM(hashrate) FROM miner_stats");
        tot_hash = cursor.fetchone()
        total = tot_hash[0]
        total_hashrate = round(total, 2)
        #print('total hash after round: ' + str(total_hashrate))
        total_hashrate = total_hashrate/1000
        hash_unit = 'Th'
        if total_hashrate > 1000:
            total_hashrate = total_hashrate/1000
            hash_unit = 'Ph'
        else:
            total_hashrate = total_hashrate
        total_hashrate = round(total_hashrate, 2)
        total_hashrate = str(total_hashrate)
        total_hashrate = total_hashrate.replace("(","").replace(")","")
        on_query = cursor.execute("SELECT COUNT(status) FROM miner_stats WHERE status = 'ONLINE'")
        on = cursor.fetchone()[0]
        off_query = cursor.execute("SELECT COUNT(status) FROM miner_stats")
        off = cursor.fetchone()[0]
        on_off = str(on) + ' / ' + str(off)
        cursor.execute("SELECT AVG(av_temp) FROM miner_stats")
        temp_av = cursor.fetchone()[0]
        temp_av = round(temp_av, 2)
        cursor.execute("SELECT SUM(num_cards) FROM miner_stats")
        card_count = cursor.fetchone()[0]
        cursor.execute('SELECT * FROM miner_stats ORDER BY INET_ATON(miner_ip)')
        #cursor.execute('SELECT * FROM miner_stats ORDER BY location')
        data = cursor.fetchall()
        cursor.execute('SELECT site FROM miner_stats LIMIT 1')
        #sitename = cursor.fetchone()[0]
        sitename = 'Quincy'
        if 'george' in str(sitename).lower():
            site_name = 'George'
        elif 'electriccity' in str(sitename).lower():
            site_name = 'Electric City'
        elif 'quincy' in str(sitename).lower():
            site_name = 'Quincy'
        if data:
            counter = len(data)
        else:
            counter = 0
        #print(counter)
        #return render_template('home/index.html', segment='index')
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Access Denied Error')
            print(err)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            print(err)
        else:
            print('Unknown Error In MySQL')
            print(err)
    except Exception as e:
        print('Had An Unknown Exception')
        print(e)
    print('len of data: ' + str(data))
    print(data)
    return render_template('home/quincy.html', title='Logixx Monitoring', hash_unit=hash_unit, site_name=site_name, users=data, total_hashrate=total_hashrate, on_off=on_off, temp_av=temp_av, card_count=card_count )

"""
    if counter != 0:
        return render_template('home/quincy.html', title='Logixx Monitoring', hash_unit=hash_unit, site_name=site_name, users=data, total_hashrate=total_hashrate.replace("(","").replace(")",""), on_off=on_off, temp_av=temp_av, card_count=card_count )
    else:
        return render_template('home/noindex.html', title='Logixx Monitoring', sitename=sitename, users=data, total_hashrate=total_hashrate.replace("(","").replace(")",""), on_off=on_off, temp_av=temp_av, card_count=card_count)

"""


@blueprint.route('/quincy')
@login_required 
def quincy():
    global hash_unit, site_name, data, total_hashrate, on_off, temp_av, card_count

    handler = logging.FileHandler("test.log")  # Create the file logger
    current_app.logger.addHandler(handler)
    current_app.logger.setLevel(logging.DEBUG)         # Set the log level to debug
    current_app.logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
    current_app.logger.info('getting quincy page')
    current_app.logger.info('route: ' + str(request.access_route) + 'blueprint: ' + str(request.blueprints) + 'cookies: ' + str(request.cookies) + 'full path' + str(request.full_path) + 'user_agent: ' + str(request.user_agent) + 'remote_addr: ' + str(request.remote_addr))

    try:
        #user = User.query
        miner_db = "quincy_miners"
        conn = mysql.connector.connect (
            host="192.168.222.13",
            user="shawnm",
            port="3306",
            password="Gr33nDr34m5!@#",
            database=miner_db,
            auth_plugin='mysql_native_password', )
        conn.autocommit = True
        cursor = conn.cursor() 
        cursor.execute("SELECT SUM(hashrate) FROM miner_stats");
        tot_hash = cursor.fetchone()
        total = tot_hash[0]
        total_hashrate = round(total, 2)
        #print('total hash after round: ' + str(total_hashrate))
        total_hashrate = total_hashrate/1000
        hash_unit = 'Th'
        if total_hashrate > 1000:
            total_hashrate = total_hashrate/1000
            hash_unit = 'Ph'
        else:
            total_hashrate = total_hashrate
        total_hashrate = round(total_hashrate, 2) 
        total_hashrate = str(total_hashrate) 
        on_query = cursor.execute("SELECT COUNT(status) FROM miner_stats WHERE status = 'ONLINE'")
        on = cursor.fetchone()[0]
        off_query = cursor.execute("SELECT COUNT(status) FROM miner_stats")
        off = cursor.fetchone()[0]
        on_off = str(on) + ' / ' + str(off)
        cursor.execute("SELECT AVG(av_temp) FROM miner_stats")
        temp_av = cursor.fetchone()[0]
        temp_av = round(temp_av, 2)
        
        cursor.execute("SELECT SUM(num_cards) FROM miner_stats")
        card_count = cursor.fetchone()[0]

        cursor.execute('SELECT * FROM miner_stats ORDER BY INET_ATON(miner_ip)')
        #cursor.execute('SELECT * FROM miner_stats ORDER BY location')
        data = cursor.fetchall()

        cursor.execute('SELECT site FROM miner_stats LIMIT 1')
        #sitename = cursor.fetchone()[0]
        sitename = 'George'
        if 'george' in str(sitename).lower():
            site_name = 'George'
        elif 'electriccity' in str(sitename).lower():
            site_name = 'Electric City'
        elif 'quincy' in str(sitename).lower():
            site_name = 'Quincy'

        if data:
            counter = len(data)
        else:
            counter = 0
        #print(counter)
        #return render_template('home/index.html', segment='index')

        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Access Denied Error')
            print(err)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            print(err)
        else:
            print('Unknown Error In MySQL')
            print(err)
    except Exception as e:
        print('Had An Unknown Exception')
        print(e)

    return render_template('home/quincy.html', title='Logixx Monitoring', hash_unit=hash_unit, site_name=site_name, users=data, total_hashrate=total_hashrate.replace("(","").replace(")",""), on_off=on_off, temp_av=temp_av, card_count=card_count )

"""
    if counter != 0:
        return render_template('home/quincy.html', title='Logixx Monitoring', hash_unit=hash_unit, site_name=site_name, users=data, total_hashrate=total_hashrate.replace("(","").replace(")",""), on_off=on_off, temp_av=temp_av, card_count=card_count )
    else:
        return render_template('home/noindex.html', title='Logixx Monitoring', sitename=sitename, users=data, total_hashrate=total_hashrate.replace("(","").replace(")",""), on_off=on_off, temp_av=temp_av, card_count=card_count)
"""

@blueprint.route('/george')
@login_required 
def george():
    global hash_unit, site_name, data, total_hashrate, on_off, temp_av, card_count

    handler = logging.FileHandler("test.log")  # Create the file logger
    current_app.logger.addHandler(handler)
    current_app.logger.setLevel(logging.DEBUG)         # Set the log level to debug
    current_app.logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
    current_app.logger.info('getting george page')
    current_app.logger.info('route: ' + str(request.access_route) + 'blueprint: ' + str(request.blueprints) + 'cookies: ' + str(request.cookies) + 'full path' + str(request.full_path) + 'user_agent: ' + str(request.user_agent) + 'remote_addr: ' + str(request.remote_addr))


    try:
        #user = User.query
        miner_db = "george_miners"
        conn = mysql.connector.connect (
            host="192.168.222.13",
            user="shawnm",
            port="3306",
            password="Gr33nDr34m5!@#",
            database=miner_db,
            auth_plugin='mysql_native_password', )
        conn.autocommit = True
        cursor = conn.cursor() 
        cursor.execute("SELECT SUM(hashrate) FROM miner_stats");
        tot_hash = cursor.fetchone()
        total = tot_hash[0]
        total_hashrate = round(total, 2)
        #print('total hash after round: ' + str(total_hashrate))
        total_hashrate = total_hashrate/1000
        hash_unit = 'Th'
        if total_hashrate > 1000:
            total_hashrate = total_hashrate/1000
            hash_unit = 'Ph'
        else: 
            total_hashrate = total_hashrate
        total_hashrate = round(total_hashrate, 2) 
        total_hashrate = str(total_hashrate) 
        on_query = cursor.execute("SELECT COUNT(status) FROM miner_stats WHERE status = 'ONLINE'")
        on = cursor.fetchone()[0]
        off_query = cursor.execute("SELECT COUNT(status) FROM miner_stats")
        off = cursor.fetchone()[0]
        on_off = str(on) + ' / ' + str(off)
        cursor.execute("SELECT AVG(av_temp) FROM miner_stats")
        temp_av = cursor.fetchone()[0]
        temp_av = round(temp_av, 2)
        
        cursor.execute("SELECT SUM(num_cards) FROM miner_stats")
        card_count = cursor.fetchone()[0]

        cursor.execute('SELECT * FROM miner_stats ORDER BY INET_ATON(miner_ip)')
        #cursor.execute('SELECT * FROM miner_stats ORDER BY location')
        data = cursor.fetchall()

        cursor.execute('SELECT site FROM miner_stats WHERE id=1')
        sitename = cursor.fetchone()
        #sitename = 'George'
        cursor.execute('SELECT site FROM miner_stats LIMIT 1')
        sitename = cursor.fetchone()[0]
        if 'george' in str(sitename).lower():
            site_name = 'George'
        elif 'electriccity' in str(sitename).lower():
            site_name = 'Electric City'
        elif 'quincy' in str(sitename).lower():
            site_name = 'Quincy'


        if data:
            counter = len(data)
        else:
            counter = 0
        #print(counter)
        #return render_template('home/index.html', segment='index')

        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Access Denied Error')
            print(err)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            print(err)
        else:
            print('Unknown Error In MySQL')
            print(err)
    except Exception as e:
        print('Had An Unknown Exception')
        print(e)

    return render_template('home/george.html', title='Logixx Monitoring', hash_unit=hash_unit,  site_name=site_name, users=data, total_hashrate=total_hashrate.replace("(","").replace(")",""), on_off=on_off, temp_av=temp_av, card_count=card_count )

"""
    if counter != 0:
        return render_template('home/george.html', title='Logixx Monitoring', hash_unit=hash_unit,  site_name=site_name, users=data, total_hashrate=total_hashrate.replace("(","").replace(")",""), on_off=on_off, temp_av=temp_av, card_count=card_count )
    else:
        return render_template('home/noindex.html', title='Logixx Monitoring', sitename=sitename, users=data, total_hashrate=total_hashrate.replace("(","").replace(")",""), on_off=on_off, temp_av=temp_av, card_count=card_count)
"""


@blueprint.route('/electriccity')
@login_required 
def electriccity():
    global hash_unit, site_name, data, total_hashrate, on_off, temp_av, card_count

    handler = logging.FileHandler("test.log")  # Create the file logger
    current_app.logger.addHandler(handler)
    current_app.logger.setLevel(logging.DEBUG)         # Set the log level to debug
    current_app.logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
    current_app.logger.info('getting electriccity page')
    current_app.logger.info('route: ' + str(request.access_route) + 'blueprint: ' + str(request.blueprints) + 'cookies: ' + str(request.cookies) + 'full path' + str(request.full_path) + 'user_agent: ' + str(request.user_agent) + 'remote_addr: ' + str(request.remote_addr))


    try:
        #user = User.query
        miner_db = "electriccity_miners"
        conn = mysql.connector.connect (
            host="192.168.222.13",
            user="shawnm",
            port="3306",
            password="Gr33nDr34m5!@#",
            database=miner_db,
            auth_plugin='mysql_native_password', )
        conn.autocommit = True
        cursor = conn.cursor() 
        cursor.execute("SELECT SUM(hashrate) FROM miner_stats");
        tot_hash = cursor.fetchone()
        total = tot_hash[0]
        total_hashrate = round(total, 2)
        #print('total hash after round: ' + str(total_hashrate))
        total_hashrate = total_hashrate/1000
        hash_unit = 'Th'
        if total_hashrate > 1000:
            total_hashrate = total_hashrate/1000
            hash_unit = 'Ph'
        else:
            total_hashrate = total_hashrate
        total_hashrate = round(total_hashrate, 2) 
        total_hashrate = str(total_hashrate) 
        on_query = cursor.execute("SELECT COUNT(status) FROM miner_stats WHERE status = 'ONLINE'")
        on = cursor.fetchone()[0]
        off_query = cursor.execute("SELECT COUNT(status) FROM miner_stats")
        off = cursor.fetchone()[0]
        on_off = str(on) + ' / ' + str(off)
        cursor.execute("SELECT AVG(av_temp) FROM miner_stats")
        temp_av = cursor.fetchone()[0]
        temp_av = round(temp_av, 2)
        
        cursor.execute("SELECT SUM(num_cards) FROM miner_stats")
        card_count = cursor.fetchone()[0]

        cursor.execute('SELECT * FROM miner_stats ORDER BY INET_ATON(miner_ip)')
        #cursor.execute('SELECT * FROM miner_stats ORDER BY location')
        data = cursor.fetchall()

        cursor.execute('SELECT site FROM miner_stats WHERE id=1')
        sitename = cursor.fetchone()

        cursor.execute('SELECT site FROM miner_stats LIMIT 1')
        sitename = cursor.fetchone()[0]
        if 'george' in str(sitename).lower():
            site_name = 'George'
        elif 'electriccity' in str(sitename).lower():
            site_name = 'Electric City'
        elif 'quincy' in str(sitename).lower():
            site_name = 'Quincy'

        if data:
            counter = len(data)
        else:
            counter = 0
        #print(counter)
        #return render_template('home/index.html', segment='index')

        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Access Denied Error')
            print(err)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            print(err)
        else:
            print('Unknown Error In MySQL')
            print(err)
    except Exception as e:
        print('Had An Unknown Exception')
        print(e)

    return render_template('home/electriccity.html', title='Logixx Monitoring', hash_unit=hash_unit,  site_name=site_name, users=data, total_hashrate=total_hashrate.replace("(","").replace(")",""), on_off=on_off, temp_av=temp_av, card_count=card_count )

"""
    if counter != 0:
        return render_template('home/electriccity.html', title='Logixx Monitoring', hash_unit=hash_unit,  site_name=site_name, users=data, total_hashrate=total_hashrate.replace("(","").replace(")",""), on_off=on_off, temp_av=temp_av, card_count=card_count )
    else:
        return render_template('home/noindex.html', title='Logixx Monitoring', sitename=sitename, users=data, total_hashrate=total_hashrate.replace("(","").replace(")",""), on_off=on_off, temp_av=temp_av, card_count=card_count)
"""



@blueprint.route('/rebooter')
@login_required
def rebooter():
    global hash_unit, site_name, data, total_hashrate, on_off, temp_av, card_count

    handler = logging.FileHandler("test.log")  # Create the file logger
    current_app.logger.addHandler(handler)
    current_app.logger.setLevel(logging.DEBUG)         # Set the log level to debug
    current_app.logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
    current_app.logger.info('getting rebooter page')
    current_app.logger.info('route: ' + str(request.access_route) + 'blueprint: ' + str(request.blueprints) + 'cookies: ' + str(request.cookies) + 'full path' + str(request.full_path) + 'user_agent: ' + str(request.user_agent) + 'remote_addr: ' + str(request.remote_addr))

    try:
        #user = User.query
        miner_db = "george_miners"
        conn = mysql.connector.connect (
            host="192.168.222.13",
            user="shawnm",
            port="3306",
            password="Gr33nDr34m5!@#",
            database=miner_db,
            auth_plugin='mysql_native_password', )
        conn.autocommit = True
        cursor = conn.cursor() 
        cursor.execute("SELECT SUM(hashrate) FROM miner_stats");
        tot_hash = cursor.fetchone()
        total = tot_hash[0]
        total_hashrate = round(total, 2)
        #print('total hash after round: ' + str(total_hashrate))
        total_hashrate = total_hashrate/1000
        hash_unit = 'Th'
        if total_hashrate > 1000:
            total_hashrate = total_hashrate/1000
            hash_unit = 'Ph'
        else:
            total_hashrate = total_hashrate
        total_hashrate = round(total_hashrate, 2) 
        total_hashrate = str(total_hashrate) 
        on_query = cursor.execute("SELECT COUNT(status) FROM miner_stats WHERE status = 'ONLINE'")
        on = cursor.fetchone()[0]
        off_query = cursor.execute("SELECT COUNT(status) FROM miner_stats")
        off = cursor.fetchone()[0]
        on_off = str(on) + ' / ' + str(off)
        cursor.execute("SELECT AVG(av_temp) FROM miner_stats")
        temp_av = cursor.fetchone()[0]
        temp_av = round(temp_av, 2)

        cursor.execute("SELECT SUM(num_cards) FROM miner_stats")
        card_count = cursor.fetchone()[0]

        cursor.execute('SELECT site FROM miner_stats WHERE id=1')
        sitename = cursor.fetchone()

        cursor.close()
        conn.close() 
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Access Denied Error')
            print(err)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            print(err)
        else:
            print('Unknown Error In MySQL')
            print(err)
    except Exception as e:
        print('Had An Unknown Exception')
        print(e)

    return render_template('home/indexRebooter.html', title='Logixx Monitoring', hash_unit=hash_unit, sitename=site_name, total_hashrate=total_hashrate.replace("(","").replace(")",""), on_off=on_off, temp_av=temp_av, card_count=card_count )





@blueprint.route('/<template>')
@login_required
def route_template(template):
    try: 
        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404
    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'

        return segment
    except:
        return None
