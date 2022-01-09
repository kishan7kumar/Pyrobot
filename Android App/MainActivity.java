package com.example.pyrobot1;
import android.graphics.Color;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.EditText;
import android.util.Log;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
public class MainActivity extends AppCompatActivity
{
    WebView live_feed;
    Button btnUp;
    Button btnDown;
    Button btnstop;
    Button btnleft;
    Button btnright;
    Button btncamup;
    Button btncamleft;
    Button btncamright;
    Button btncamdown;
    Button btnfireon;
    Button btnfireoff;
    Button btnx;
    Button btny;
    Button btndleft;
    Button btndright;
    Button btngateopen;
    Button btngateclose;

    EditText txtAddress;
    Socket myAppSocket = null;
    public static String wifiModuleIp = "";
    public static int wifiModulePort = 0;
    public static String command = "0";
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.activity_main);
        getSupportActionBar().hide();
        live_feed  = (WebView) findViewById(R.id.webView);
        live_feed.setBackgroundColor(Color.TRANSPARENT);
        live_feed.loadUrl("http://172.20.10.4:8081");  // ip address of the bot and port for webcam server
        btnUp = (Button) findViewById(R.id.btnUp);
        btnDown = (Button) findViewById(R.id.btnDown);
        btnstop = (Button) findViewById(R.id.btnstop);
        btnleft = (Button) findViewById(R.id.btnleft);
        btnright = (Button) findViewById(R.id.btnright);
        txtAddress = (EditText) findViewById(R.id.ipAddress);

        btncamup = (Button) findViewById(R.id.btncamup);
        btncamdown = (Button) findViewById(R.id.btncamdown);
        btncamleft = (Button) findViewById(R.id.btncamleft);
        btncamright = (Button) findViewById(R.id.btncamright);
        btnfireon = (Button) findViewById(R.id.btnfireon);
        btnfireoff = (Button) findViewById(R.id.btnfireoff);
        btnx = (Button) findViewById(R.id.btnx);
        btny = (Button) findViewById(R.id.btny);
        btndleft = (Button) findViewById(R.id.btndleft);
        btndright = (Button) findViewById(R.id.btndright);

        btngateopen = (Button) findViewById(R.id.btngateopen);
        btngateclose = (Button) findViewById(R.id.btngateclose);

        btngateopen.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command = "16";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });

        btngateclose.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command = "17";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });


        btndleft.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command = "14";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });

        btndright.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command = "15";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });





        btnx.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command = "12";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });

        btny.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command = "13";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });


        btncamup.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command = "6";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });

        btncamdown.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command = "7";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });

        btncamleft.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command = "8";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });

        btncamright.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command = "9";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });

        btnfireon.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command = "10";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });

        btnfireoff.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command = "11";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });

        btnUp.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command = "1";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });
        btnDown.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command= "2";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });
        btnstop.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command= "3";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });
        btnleft.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command = "4";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });
        btnright.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                getIPandPort();
                command = "5";
                Socket_AsyncTask control_command = new Socket_AsyncTask();
                control_command.execute();
            }
        });
    }
    public void getIPandPort()
    {
        String iPandPort = txtAddress.getText().toString();
        Log.d("DOING TEST","IP String: "+ iPandPort);
        String temp[]= iPandPort.split(":");
        wifiModuleIp = temp[0];
        wifiModulePort = Integer.valueOf(temp[1]);
        Log.d("DOING TEST","IP:" +wifiModuleIp);
        Log.d("DOING TEST","PORT:"+wifiModulePort);
    }


    public class Socket_AsyncTask extends AsyncTask<Void,Void,Void>
    {
        Socket socket;

        @Override
        protected Void doInBackground(Void... params)
        {
            try
            {
                InetAddress inetAddress = InetAddress.getByName(MainActivity.wifiModuleIp);
                socket = new java.net.Socket(inetAddress, MainActivity.wifiModulePort);
                DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());
                dataOutputStream.writeBytes(command);
                dataOutputStream.close();
                socket.close();

            }
            catch (UnknownHostException e)
            {
                e.printStackTrace();
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
            return null;
        }
    }
}
