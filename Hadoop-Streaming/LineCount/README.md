This example shows a hadoop streaming job in Python making use of python virtual environment and distributed cache. 

Set up a python virtual environment as described in http://documentation.altiscale.com/using-python.

Run the following command to run this example. 

hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar -files ml.py,rl.py -archives hdfs:///user/alti_ranjana/myenv.zip#py279 -mapper ml.py -reducer rl.py -input hdfs:///mr-history/logs/alti_ranjana/logs/application_1446764629008_0666/202-02.as1.altiscale.com_21562 -output linecount
