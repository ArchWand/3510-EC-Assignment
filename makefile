BIN=runcpp
JAR=run.jar
JAVADIR=parsers/java

${BIN}: parsers/cpp/*.cpp parsers/cpp/*.h src/Solutions.cpp
	g++ -std=c++17 -o ${BIN} parsers/cpp/run.cpp src/Solutions.cpp -O2

.PHONY: debug
debug:
	g++ -std=c++17 -g -o ${BIN} parsers/cpp/run.cpp src/Solutions.cpp -g -fsanitize=address

.PHONY: clean
clean:
	rm -f ${BIN} ${JAR} ${JAVADIR}/*.class ${JAVADIR}/${JAR}

.PHONY: jar
jar: ${JAR}
run.jar: ${JAVADIR}/run.class
	cd ${JAVADIR} && jar -cvfe ${JAR} run *.class
	cp -f ${JAVADIR}/${JAR} .

${JAVADIR}/run.class: ${JAVADIR}/*.java src/Solutions.java
	cd ${JAVADIR} && javac run.java

