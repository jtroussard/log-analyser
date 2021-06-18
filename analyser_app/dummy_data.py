dummy_data = [
{
	"id": 1,
    "description": "[com.techrx.security.SymmetricEncryptor] (default task-13)",
    "details": "|BL:|TS:6/1/21 3:40:57 PM EDT|LL:SEVERE|TM:127.0.1.1-1622576457260|CN:com.techrx.security.SymmetricEncryptor|MT:loadKeyMap|MSG Could not load key map successfully.  Please make sure symmetric key store is set up|EX:",
    "stacktace": "java.lang.StringIndexOutOfBoundsException: String index out of range: -1\
	at java.lang.String.substring(String.java:1931)\
	at com.techrx.security.SymmetricEncryptor.loadKeyMap(SymmetricEncryptor.java:208)\
	at com.techrx.security.SymmetricEncryptor.init(SymmetricEncryptor.java:94)\
	at com.techrx.security.SymmetricEncryptor.<init>(SymmetricEncryptor.java:63)\
	at com.techrx.security.SymmetricEncryptor.<clinit>(SymmetricEncryptor.java:55)\
	at com.techrx.model.service.tools.login.LoginPersistorImpl.getLoginInfo(LoginPersistorImpl.java:275)\
	at com.techrx.model.service.tools.login.LoginServiceImpl.login(LoginServiceImpl.java:172)\
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)\
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)\
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)\
	at java.lang.reflect.Method.invoke(Method.java:498)\
	at com.techrx.model.service.ServiceSB.callService(ServiceSB.java:83)\
	at com.techrx.model.service.ServiceSB.nonTransactionService(ServiceSB.java:65)\
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)\
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)\
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)\
	at java.lang.reflect.Method.invoke(Method.java:498)\
	at org.jboss.as.ee.component.ManagedReferenceMethodInterceptor.processInvocation(ManagedReferenceMethodInterceptor.java:52)\
	at org.jboss.invocation.InterceptorContext.proceed(InterceptorContext.java:422)\
	at org.jboss.invocation.InterceptorContext$Invocation.proceed(InterceptorContext.java:509)\
	at org.jboss.as.weld.interceptors.Jsr299BindingsInterceptor.doMethodInterception(Jsr299BindingsInterceptor.java:90)\
	at org.jboss.as.weld.interceptors.Jsr299BindingsInterceptor.processInvocation(Jsr299BindingsInterceptor.java:101)\
	at org.jboss.as.ee.component.interceptors.UserInterceptorFactory$1.processInvocation(UserInterceptorFactory.java:63)",
	"add_jira_ticket_button": True,
	"add_confluence_row": True,
},
{
	"id": 2,
    "description": "[com.techrx.soap.handler.ExceptionHandler] (default task-13) ",
    "details": "|BL:|TS:6/1/21 3:40:57 PM EDT|LL:SEVERE|TM:127.0.1.1-1622576457260|CN:com.techrx.soap.handler.ExceptionHandler|MT:handleException|MSG:Error processing request|EX:",
    "stacktace": "	java.lang.StringIndexOutOfBoundsException: String index out of range: -1\
		at java.lang.String.substring(String.java:1931)\
		at com.techrx.security.SymmetricEncryptor.loadKeyMap(SymmetricEncryptor.java:208)\
		at com.techrx.security.SymmetricEncryptor.init(SymmetricEncryptor.java:94)\
		at com.techrx.security.SymmetricEncryptor.<init>(SymmetricEncryptor.java:63)\
		at com.techrx.security.SymmetricEncryptor.<clinit>(SymmetricEncryptor.java:55)\
		at com.techrx.model.service.tools.login.LoginPersistorImpl.getLoginInfo(LoginPersistorImpl.java:275)\
		at com.techrx.model.service.tools.login.LoginServiceImpl.login(LoginServiceImpl.java:172)\
		at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)\
		at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)\
		at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)\
		at java.lang.reflect.Method.invoke(Method.java:498)\
		at com.techrx.model.service.ServiceSB.callService(ServiceSB.java:83)\
		at com.techrx.model.service.ServiceSB.nonTransactionService(ServiceSB.java:65)\
		at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)",
	"add_jira_ticket_button": True,
	"add_confluence_row": False,
},
]