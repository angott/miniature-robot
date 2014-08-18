#!/usr/bin/python 
import sys
import pygame
import math
import types
import mutable

class CollisionModel:
    'Class for collision detection'
        
    def CircleTouchesLine(self, A, B, C, r ):
        result = types.SimpleNamespace()
        result.inside = False
        result.tangent = False
        result.intersects = False
        result.enter = None
        result.out = None
        a = (B.x - A.x) * (B.x - A.x) + (B.y - A.y) * (B.y - A.y)
        b = 2 * ((B.x - A.x) * (A.x - C.x) +(B.y - A.y) * (A.y - C.y))
        cc = C.x * C.x + C.y * C.y + A.x * A.x + A.y * A.y - 2 * (C.x * A.x + C.y * A.y) - r * r
        deter = b * b - 4 * a * cc
        if (deter <= 0 ):
            result.inside = False
        else:
            e = math.sqrt (deter)
            u1 = ( - b + e ) / (2 * a )
            u2 = ( - b - e ) / (2 * a )
            if ((u1 < 0 or u1 > 1) and (u2 < 0 or u2 > 1)):
                if ((u1 < 0 and u2 < 0) or (u1 > 1 and u2 > 1)):
                    result.inside = False
                else:
                    result.inside = True
            else:
 #               if (0 <= u2 and u2 <= 1):
 #			    result.enter=Point.interpolate (A, B, 1 - u2)

 #               if (0 <= u1 and u1 <= 1):
 #                   result.exit=Point.interpolate (A, B, 1 - u1)
                    
                result.intersects = True
                if (result.out != None and result.enter != None and result.out.equals (result.enter)) :
                    result.tangent = True		
        return result
