<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="WK9-D2-FlowchartListExercise3-Espiritu"/>
        <attribute name="authors" value="jeffe"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2026-10-01 12:37:44 am"/>
        <attribute name="created" value="amVmZmU7TVNJOzIwMjYtMTAtMDE7MTI6MTI6MTggYW07MjA2NQ=="/>
        <attribute name="edited" value="amVmZmU7TVNJOzIwMjYtMTAtMDE7MTI6Mzc6NDQgYW07MjsyMTgw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="rainbowColors" type="String" array="True" size="7"/>
            <declare name="userName" type="String" array="False" size=""/>
            <declare name="userGuesses" type="String" array="True" size="7"/>
            <declare name="correctCount" type="Integer" array="False" size=""/>
            <declare name="grade" type="String" array="False" size=""/>
            <assign variable="rainbowColors[0]" expression="&quot;red&quot;"/>
            <assign variable="rainbowColors[1]" expression="&quot;orange&quot;"/>
            <assign variable="rainbowColors[2]" expression="&quot;yellow&quot;"/>
            <assign variable="rainbowColors[3]" expression="&quot;green&quot;"/>
            <assign variable="rainbowColors[4]" expression="&quot;blue&quot;"/>
            <assign variable="rainbowColors[5]" expression="&quot;indigo&quot;"/>
            <assign variable="rainbowColors[6]" expression="&quot;violet&quot;"/>
            <assign variable="userName" expression="GetUserName()"/>
            <call expression="GetGuesses(userGuesses)"/>
            <assign variable="correctCount" expression="CountCorrect(rainbowColors, userGuesses)"/>
            <assign variable="grade" expression="GetGrade(correctCount)"/>
            <output expression="&quot;Hello &quot; &amp; userName &amp; &quot;! You guessed &quot; &amp; correctCount &amp; &quot; out of 7 colors correctly. Your grade is: &quot; &amp; grade &amp; &quot;.&quot;" newline="True"/>
        </body>
    </function>
    <function name="CountCorrect" type="Integer" variable="correctCount">
        <parameters>
            <parameter name="rainbowColors" type="String" array="True"/>
            <parameter name="userGuesses" type="String" array="True"/>
        </parameters>
        <body>
            <declare name="correctCount" type="Integer" array="False" size=""/>
            <declare name="i" type="Integer" array="False" size=""/>
            <assign variable="correctCount" expression="0"/>
            <for variable="i" start="0" end="6" direction="inc" step="1">
                <if expression="userGuesses[i] == rainbowColors[i]">
                    <then>
                        <assign variable="correctCount" expression="correctCount + 1"/>
                    </then>
                    <else/>
                </if>
            </for>
        </body>
    </function>
    <function name="GetGrade" type="String" variable="grade">
        <parameters>
            <parameter name="score" type="Integer" array="False"/>
        </parameters>
        <body>
            <declare name="grade" type="String" array="False" size=""/>
            <if expression="score &gt;= 6">
                <then>
                    <assign variable="grade" expression="&quot;excellent&quot;"/>
                </then>
                <else>
                    <if expression="score &gt;= 3">
                        <then>
                            <assign variable="grade" expression="&quot;average&quot;"/>
                        </then>
                        <else>
                            <assign variable="grade" expression="&quot;poor&quot;"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
    <function name="GetGuesses" type="None" variable="">
        <parameters>
            <parameter name="userGuesses" type="String" array="True"/>
        </parameters>
        <body>
            <declare name="i" type="Integer" array="False" size=""/>
            <for variable="i" start="0" end="6" direction="inc" step="1">
                <output expression="&quot;Enter color guess #&quot; &amp; (i + 1) &amp; &quot;:&quot;" newline="True"/>
                <input variable="userGuesses[i]"/>
            </for>
        </body>
    </function>
    <function name="GetUserName" type="String" variable="userName">
        <parameters/>
        <body>
            <declare name="userName" type="String" array="False" size=""/>
            <output expression="&quot;Please enter your name:&quot;" newline="True"/>
            <input variable="userName"/>
        </body>
    </function>
</flowgorithm>
