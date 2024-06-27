skills = [
    "ROS",
    "C++",
    "Python",
    "TensorFlow",
    "PyTorch",
    "Keras",
    "Matlab",
    "Simulink",
    "Linux",
    "Git",
    "Bash",
    "Docker",
    "OpenCV",
    "SLAM",
    "VHDL",
    "Verilog",
    "FPGA",
    "CUDA",
    "Caffe",
    "Scikit-learn",
    "Pandas",
    "NumPy",
    "SciPy",
    "R",
    "Java",
    "C",
    "SQL",
    "NoSQL",
    "Hadoop",
    "Spark",
    "Tableau",
    "Matplotlib",
    "Seaborn",
    "NLTK",
    "Spacy",
    "Selenium",
    "Jupyter",
    "Arduino",
    "RaspberryPi",
    "TensorRT",
    "ONNX",
    "GCP",
    "AWS",
    "Azure",
    "Kubernetes",
    "Ansible",
    "Terraform",
    "Jenkins",
    "Flask",
    "Django",
    "FastAPI",
    "REST",
    "GraphQL",
    "HDFS",
    "Hive",
    "Pig",
    "Mahout",
    "SparkML",
    "MLlib",
    "Kafka",
    "RabbitMQ",
    "Celery",
    "Elasticsearch",
    "Logstash",
    "Kibana",
    "Prometheus",
    "Grafana",
    "Airflow",
    "ETL",
    "Redux",
    "React",
    "Vue",
    "Angular",
    "Bootstrap",
    "HTML",
    "CSS",
    "JavaScript",
    "TypeScript",
    "Perl",
    "Go",
    "Ruby",
    "Scala",
    "Lua",
    "Shell",
    "PowerShell",
    "ObjectiveC",
    "Swift",
    "Android",
    "iOS",
    "Xcode",
    "Unity",
    "Blender",
    "Gazebo",
    "Autonomous",
    "LIDAR",
    "RADAR",
    "Sonar",
    "ZMQ",
    "Protobuf",
    "Thrift",
    "Hadoop",
    "MapReduce",
    "ROS-MoveIt!",
    "PHP"
]

def get_skills(resume_text):
    skills_found = []
    for skill in skills:
        if skill in resume_text:
            skills_found.append(skill)
    return skills_found
