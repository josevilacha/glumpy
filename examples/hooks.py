#! /usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import glumpy
import glumpy.gloo as gloo

vertex = (
"""
attribute vec2 position;
void main()
{ gl_Position = <transform.forward>; }
""")

fragment = (
"""
void main()
{ gl_FragColor = <color>; }
""")

position2D = gloo.Snippet(
"""
vec4 position2D(vec2 position)
{ return vec4(position, 0.0, 1.0); }
""")

translate = gloo.Snippet(
"""
uniform vec3 translate;

vec4 forward(vec4 position)
{ return vec4(position.xyz+translate, 1.0); }

vec4 inverse(vec4 position)
{ return vec4(position.xyz-translate, 1.0); }
""")

#print translate(position2D("position"), translate="offset").code
window = glumpy.Window()

program = gloo.Program(vertex, fragment)
program["transform"] = translate(position2D("position"))
program["transform"]["translate"] = 1
program["translate"] = 1
program["color"] = "vec4(0,0,0,1)"
print program._verts[0].code

print "---"

program = gloo.Program(vertex, fragment)
program["transform"] = translate(position2D("position"), translate="offset")
program["transform"]["offset"] = 1
program["offset"] = 1
program["color"] = "vec4(0,0,0,1)"
print program._verts[0].code
