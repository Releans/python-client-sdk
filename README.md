# Getting started

The Releans SDK enables developers to use Releans Services in their code. You can get started in minutes.

## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=Releans-Python)


## How to Use

The following section explains how to use the Releans SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your Releans SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=Releans-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=Releans-Python&projectName=releans)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=Releans-Python&projectName=releans)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=Releans-Python&projectName=releans)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the Releans python library using the following code lines

```Python
from releans.releans import Releans
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=Releans-Python&libraryName=releans.releans&projectName=releans&className=Releans)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=Releans-Python&libraryName=releans.releans&projectName=releans&className=Releans)


## How to Test

You can test the Releans SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| o_auth_access_token | OAuth 2.0 Access Token |



API client can be initialized as following.

```python
# Configuration parameters and credentials
o_auth_access_token = 'o_auth_access_token' # OAuth 2.0 Access Token

client = Releans(o_auth_access_token)
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [MessageController](#message_controller)
* [SenderController](#sender_controller)
* [BalanceController](#balance_controller)

## <a name="message_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MessageController") MessageController

### Get controller instance

An instance of the ``` MessageController ``` class can be accessed from the API Client.

```python
 message_controller = client.message
```

### <a name="get_all_messages"></a>![Method: ](https://apidocs.io/img/method.png ".MessageController.get_all_messages") get_all_messages

> List all messages sent by the account.

```python
def get_all_messages(self)
```

#### Example Usage

```python

result = message_controller.get_all_messages()

```


### <a name="get_price_of_message"></a>![Method: ](https://apidocs.io/img/method.png ".MessageController.get_price_of_message") get_price_of_message

> Return cost of sending a message to the number.

```python
def get_price_of_message(self,
                             mobile_number)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mobileNumber |  ``` Required ```  | Mobile number you want to know the price of sending a message. |



#### Example Usage

```python
mobile_number = 'mobileNumber'

result = message_controller.get_price_of_message(mobile_number)

```


### <a name="get_view_message"></a>![Method: ](https://apidocs.io/img/method.png ".MessageController.get_view_message") get_view_message

> Return the details of the message.

```python
def get_view_message(self,
                         id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  ``` DefaultValue ```  | Id of the message you need to return its details. |



#### Example Usage

```python
id = 'id'

result = message_controller.get_view_message(id)

```


### <a name="create_send_sms_message"></a>![Method: ](https://apidocs.io/img/method.png ".MessageController.create_send_sms_message") create_send_sms_message

> Send a single message.

```python
def create_send_sms_message(self,
                                sender_id,
                                mobile_number,
                                message)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| senderId |  ``` Required ```  ``` DefaultValue ```  | Sender id to send the message from. |
| mobileNumber |  ``` Required ```  ``` DefaultValue ```  | The mobile number supposed to receive the message. |
| message |  ``` Required ```  ``` DefaultValue ```  | Message text. |



#### Example Usage

```python
sender_id = 'sender-id'
mobile_number = 'mobile-number'
message = 'message'

result = message_controller.create_send_sms_message(sender_id, mobile_number, message)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="sender_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SenderController") SenderController

### Get controller instance

An instance of the ``` SenderController ``` class can be accessed from the API Client.

```python
 sender_controller = client.sender
```

### <a name="get_sender_name_details"></a>![Method: ](https://apidocs.io/img/method.png ".SenderController.get_sender_name_details") get_sender_name_details

> Return the details of the sender name.

```python
def get_sender_name_details(self,
                                id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  ``` DefaultValue ```  | The sender id you want its details |



#### Example Usage

```python
id = 'sender-id'

result = sender_controller.get_sender_name_details(id)

```


### <a name="create_sender_name"></a>![Method: ](https://apidocs.io/img/method.png ".SenderController.create_sender_name") create_sender_name

> Create a new sender id to send messages using it

```python
def create_sender_name(self,
                           sender_name)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| senderName |  ``` Required ```  ``` DefaultValue ```  | Name you want to register as Sender Name |



#### Example Usage

```python
sender_name = 'Your sender name'

result = sender_controller.create_sender_name(sender_name)

```


### <a name="get_all_senders"></a>![Method: ](https://apidocs.io/img/method.png ".SenderController.get_all_senders") get_all_senders

> List all senders names associated with the account

```python
def get_all_senders(self)
```

#### Example Usage

```python

result = sender_controller.get_all_senders()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="balance_controller"></a>![Class: ](https://apidocs.io/img/class.png ".BalanceController") BalanceController

### Get controller instance

An instance of the ``` BalanceController ``` class can be accessed from the API Client.

```python
 balance_controller = client.balance
```

### <a name="get_balance"></a>![Method: ](https://apidocs.io/img/method.png ".BalanceController.get_balance") get_balance

> Get your available balance

```python
def get_balance(self)
```

#### Example Usage

```python

result = balance_controller.get_balance()

```


[Back to List of Controllers](#list_of_controllers)



